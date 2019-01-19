# Terraform::AWS::TransferUser

Provides a AWS Transfer User resource. Managing SSH keys can be accomplished with the [`aws_transfer_ssh_key` resource](/docs/providers/aws/r/transfer_ssh_key.html).


```hcl
resource "aws_transfer_server" "foo" {
	identity_provider_type = "SERVICE_MANAGED"

	tags {
		NAME     = "tf-acc-test-transfer-server"
	}
}

resource "aws_iam_role" "foo" {
	name = "tf-test-transfer-user-iam-role"

	assume_role_policy = <<EOF
{
	"Version": "2012-10-17",
	"Statement": [
		{
		"Effect": "Allow",
		"Principal": {
			"Service": "transfer.amazonaws.com"
		},
		"Action": "sts:AssumeRole"
		}
	]
}
EOF
}

resource "aws_iam_role_policy" "foo" {
	name = "tf-test-transfer-user-iam-policy"
	role = "${aws_iam_role.foo.id}"
	policy = <<POLICY
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "AllowFullAccesstoS3",
			"Effect": "Allow",
			"Action": [
				"s3:*"
			],
			"Resource": "*"
		}
	]
}
POLICY
}

resource "aws_transfer_user" "foo" {
	server_id      = "${aws_transfer_server.foo.id}"
	user_name      = "tftestuser"
	role           = "${aws_iam_role.foo.arn}"
}

```

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - Amazon Resource Name (ARN) of Transfer User.

## See Also

* [aws_transfer_user](https://www.terraform.io/docs/providers/aws/r/transfer_user.html) in the _Terraform Provider Documentation_
# Terraform::AWS::TransferUser

Provides a AWS Transfer User resource. Managing SSH keys can be accomplished with the [`Terraform::AWS::TransferSshKey` resource](/docs/providers/aws/r/transfer_ssh_key.html).


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

## Properties

`ServerId` - (Requirement) The Server ID of the Transfer Server (e.g. `s-12345678`).

`UserName` - (Requirement) The name used for log in to your SFTP server.

`HomeDirectory` - (Optional) The landing directory (folder) for a user when they log in to the server using their SFTP client.

`Policy` - (Optional) An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`. Since the IAM variable syntax matches Terraform's interpolation syntax, they must be escaped inside Terraform configuration strings (`$${Transfer:UserName}`).

`Role` - (Requirement) Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of Transfer User.

## See Also

* [aws_transfer_user](https://www.terraform.io/docs/providers/aws/r/transfer_user.html) in the _Terraform Provider Documentation_
# Terraform::AWS::TransferServer

Provides a AWS Transfer Server resource.


```hcl
resource "aws_iam_role" "foo" {
	name = "tf-test-transfer-server-iam-role"
  
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
	name = "tf-test-transfer-server-iam-policy-%s"
	role = "${aws_iam_role.foo.id}"
	policy = <<POLICY
{
	"Version": "2012-10-17",
	"Statement": [
		{
		"Sid": "AllowFullAccesstoCloudWatchLogs",
		"Effect": "Allow",
		"Action": [
			"logs:*"
		],
		"Resource": "*"
		}
	]
}
POLICY
}


resource "aws_transfer_server" "foo" {
  identity_provider_type = "SERVICE_MANAGED"
  logging_role = "${aws_iam_role.foo.arn}"

  tags {
	NAME   = "tf-acc-test-transfer-server"
	ENV    = "test"
  }
}
```

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - Amazon Resource Name (ARN) of Transfer Server.

`Id` - The Server ID of the Transfer Server (e.g. `s-12345678`).

`Endpoint` - The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`).

## See Also

* [aws_transfer_server](https://www.terraform.io/docs/providers/aws/r/transfer_server.html) in the _Terraform Provider Documentation_
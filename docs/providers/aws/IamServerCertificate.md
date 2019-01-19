# Terraform::AWS::IamServerCertificate

Provides an IAM Server Certificate resource to upload Server Certificates.
Certs uploaded to IAM can easily work with other AWS services such as:

- AWS Elastic Beanstalk
- Elastic Load Balancing
- CloudFront
- AWS OpsWorks

For information about server certificates in IAM, see [Managing Server
Certificates][2] in AWS Documentation.

~> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The unique Server Certificate name.

`Name` - The name of the Server Certificate.

`Arn` - The Amazon Resource Name (ARN) specifying the server certificate.

## See Also

* [aws_iam_server_certificate](https://www.terraform.io/docs/providers/aws/r/iam_server_certificate.html) in the _Terraform Provider Documentation_
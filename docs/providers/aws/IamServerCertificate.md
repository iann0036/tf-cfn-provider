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

`Name` - (Optional) The name of the Server Certificate. Do not include the path in this value. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`Path` - (Optional) The IAM path for the server certificate.  If it is not included, it defaults to a slash (/). If this certificate is for use with AWS CloudFront, the path must be in format `/cloudfront/your_path_here`. See [IAM Identifiers][1] for more details on IAM Paths.


## Return Values

### Fn::GetAtt

`Id` - The unique Server Certificate name.

`Name` - The name of the Server Certificate.

`Arn` - The Amazon Resource Name (ARN) specifying the server certificate.

## See Also

* [aws_iam_server_certificate](https://www.terraform.io/docs/providers/aws/r/iam_server_certificate.html) in the _Terraform Provider Documentation_
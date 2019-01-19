# Terraform::AWS::CodecommitRepository

Provides a CodeCommit Repository Resource.

~> **NOTE on CodeCommit Availability**: The CodeCommit is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`RepositoryId` - The ID of the repository.

`Arn` - The ARN of the repository.

`CloneUrlHttp` - The URL to use for cloning the repository over HTTPS.

`CloneUrlSsh` - The URL to use for cloning the repository over SSH.

## See Also

* [aws_codecommit_repository](https://www.terraform.io/docs/providers/aws/r/codecommit_repository.html) in the _Terraform Provider Documentation_
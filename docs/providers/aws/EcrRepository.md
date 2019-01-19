# Terraform::AWS::EcrRepository

Provides an EC2 Container Registry Repository.

~> **NOTE on ECR Availability**: The EC2 Container Registry is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#ecr_region).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - Full ARN of the repository.

`Name` - The name of the repository.

`RegistryId` - The registry ID where the repository was created.

`RepositoryUrl` - The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`.

## See Also

* [aws_ecr_repository](https://www.terraform.io/docs/providers/aws/r/ecr_repository.html) in the _Terraform Provider Documentation_
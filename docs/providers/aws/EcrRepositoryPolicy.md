# Terraform::AWS::EcrRepositoryPolicy

Provides an ECR repository policy.

Note that currently only one policy may be applied to a repository.

~> **NOTE on ECR Availability**: The EC2 Container Registry is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#ecr_region).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Repository` - The name of the repository.

`RegistryId` - The registry ID where the repository was created.

## See Also

* [aws_ecr_repository_policy](https://www.terraform.io/docs/providers/aws/r/ecr_repository_policy.html) in the _Terraform Provider Documentation_
# Terraform::AWS::EcrLifecyclePolicy

Manages an ECR repository lifecycle policy.

~> **NOTE:** Only one `aws_ecr_lifecycle_policy` resource can be used with the same ECR repository. To apply multiple rules, they must be combined in the `policy` JSON.

~> **NOTE:** The AWS ECR API seems to reorder rules based on `rulePriority`. If you define multiple rules that are not sorted in ascending `rulePriority` order in the Terraform code, the resource will be flagged for recreation every `terraform plan`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Repository` - The name of the repository.

`RegistryId` - The registry ID where the repository was created.

## See Also

* [aws_ecr_lifecycle_policy](https://www.terraform.io/docs/providers/aws/r/ecr_lifecycle_policy.html) in the _Terraform Provider Documentation_
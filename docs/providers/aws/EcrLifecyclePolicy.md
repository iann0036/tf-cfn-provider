# Terraform::AWS::EcrLifecyclePolicy

Manages an ECR repository lifecycle policy.

~> **NOTE:** Only one `Terraform::AWS::EcrLifecyclePolicy` resource can be used with the same ECR repository. To apply multiple rules, they must be combined in the `Policy` JSON.

~> **NOTE:** The AWS ECR API seems to reorder rules based on `rulePriority`. If you define multiple rules that are not sorted in ascending `rulePriority` order in the Terraform code, the resource will be flagged for recreation every `terraform plan`.

## Properties

`Repository` - (Required) Name of the repository to apply the policy.

`Policy` - (Required) The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).


## Return Values

### Fn::GetAtt

`Repository` - The name of the repository.

`RegistryId` - The registry ID where the repository was created.

## See Also

* [aws_ecr_lifecycle_policy](https://www.terraform.io/docs/providers/aws/r/ecr_lifecycle_policy.html) in the _Terraform Provider Documentation_
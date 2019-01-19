# Terraform::AWS::DlmLifecyclePolicy

Provides a [Data Lifecycle Manager (DLM) lifecycle policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) for managing snapshots.

## Properties

`Description` - (Required) A description for the DLM lifecycle policy.

`ExecutionRoleArn` - (Required) The ARN of an IAM role that is able to be assumed by the DLM service.

`PolicyDetails` - (Required) See the [`PolicyDetails` configuration](#policy-details-arguments) block. Max of 1.

`State` - (Optional) Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.


## See Also

* [aws_dlm_lifecycle_policy](https://www.terraform.io/docs/providers/aws/r/dlm_lifecycle_policy.html) in the _Terraform Provider Documentation_
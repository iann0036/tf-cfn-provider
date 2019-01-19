# Terraform::AWS::AutoscalingLifecycleHook

Provides an AutoScaling Lifecycle Hook resource.

~> **NOTE:** Terraform has two types of ways you can add lifecycle hooks - via
the `initial_lifecycle_hook` attribute from the
[`Terraform::AWS::AutoscalingGroup`](/docs/providers/aws/r/autoscaling_group.html)
resource, or via this one. Hooks added via this resource will not be added
until the autoscaling group has been created, and depending on your
[capacity](/docs/providers/aws/r/autoscaling_group.html#waiting-for-capacity)
settings, after the initial instances have been launched, creating unintended
behavior. If you need hooks to run on all instances, add them with
`initial_lifecycle_hook` in
[`Terraform::AWS::AutoscalingGroup`](/docs/providers/aws/r/autoscaling_group.html),
but take care to not duplicate those hooks with this resource.

## Properties

`Name` - (Required) The name of the lifecycle hook.

`AutoscalingGroupName` - (Required) The name of the Auto Scaling group to which you want to assign the lifecycle hook.

`DefaultResult` - (Optional) Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.

`HeartbeatTimeout` - (Optional) Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter.

`LifecycleTransition` - (Required) The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples).

`NotificationMetadata` - (Optional) Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.

`NotificationTargetArn` - (Optional) The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.

`RoleArn` - (Optional) The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.


## See Also

* [aws_autoscaling_lifecycle_hook](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html) in the _Terraform Provider Documentation_
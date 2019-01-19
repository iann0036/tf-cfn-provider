# Terraform::Alicloud::EssLifecycleHook

Provides a ESS lifecycle hook resource. More about Ess lifecycle hook, see [LifecycleHook](https://www.alibabacloud.com/help/doc-detail/73839.htm).

## Properties

`ScalingGroupId` - (Required, ForceNew) The ID of the Auto Scaling group to which you want to assign the lifecycle hook.

`Name` - (Optional, ForceNew) The name of the lifecycle hook, which is a string containing 2 to 40 English or Chinese characters. If this parameter value is not specified, the default value is lifecycle hook id.

`LifecycleTransition` - (Required) Type of Scaling activity attached to lifecycle hook. Supported value: SCALE_OUT, SCALE_IN.

`HeartbeatTimeout` - (Optional) Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the default_result parameter. Default value: 600.

`DefaultResult` - (Optional) Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses. Applicable value: CONTINUE, ABANDON, default value: CONTINUE.

`NotificationArn` - (Optional) The Arn of notification target.

`NotificationMetadata` - (Optional) Additional information that you want to include when Auto Scaling sends a message to the notification target.


## See Also

* [alicloud_ess_lifecycle_hook](https://www.terraform.io/docs/providers/alicloud/r/ess_lifecycle_hook.html) in the _Terraform Provider Documentation_
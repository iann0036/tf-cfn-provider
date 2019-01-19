# Terraform::AWS::AppautoscalingPolicy

Provides an Application AutoScaling Policy resource.

## Properties

`Name` - (Required) The name of the policy.

`PolicyType` - (Optional) For DynamoDB, only `TargetTrackingScaling` is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both `StepScaling` and `TargetTrackingScaling` are supported. For any other service, only `StepScaling` is supported. Defaults to `StepScaling`.

`ResourceId` - (Required) The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters).

`ScalableDimension` - (Required) The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters).

`ServiceNamespace` - (Required) The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters).

`StepScalingPolicyConfiguration` - (Optional) Step scaling policy configuration, requires `policy_type = "StepScaling"` (default). See supported fields below.

`TargetTrackingScalingPolicyConfiguration` - (Optional) A target tracking policy, requires `policy_type = "TargetTrackingScaling"`. See supported fields below.


## See Also

* [aws_appautoscaling_policy](https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html) in the _Terraform Provider Documentation_
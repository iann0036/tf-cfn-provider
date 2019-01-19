# Terraform::AWS::AppautoscalingTarget

Provides an Application AutoScaling ScalableTarget resource. To manage policies which get attached to the target, see the [`Terraform::AWS::AppautoscalingPolicy` resource](/docs/providers/aws/r/appautoscaling_policy.html).

## Properties

`MaxCapacity` - (Required) The max capacity of the scalable target.

`MinCapacity` - (Required) The min capacity of the scalable target.

`ResourceId` - (Required) The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the `ResourceId` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters).

`RoleArn` - (Optional) The ARN of the IAM role that allows Application AutoScaling to modify your scalable target on your behalf.

`ScalableDimension` - (Required) The scalable dimension of the scalable target. Documentation can be found in the `ScalableDimension` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters).

`ServiceNamespace` - (Required) The AWS service namespace of the scalable target. Documentation can be found in the `ServiceNamespace` parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters).


## See Also

* [aws_appautoscaling_target](https://www.terraform.io/docs/providers/aws/r/appautoscaling_target.html) in the _Terraform Provider Documentation_
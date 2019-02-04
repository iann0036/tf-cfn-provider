# Terraform::AWS::AutoscalingPolicy

Provides an AutoScaling Scaling Policy resource.

~> **NOTE:** You may want to omit `desired_capacity` attribute from attached `Terraform::AWS::AutoscalingGroup`
when using autoscaling policies. It's good practice to pick either
[manual](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html)
or [dynamic](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html)
(policy-based) scaling.

## Properties

`Name` - (Required) The name of the policy.

`AutoscalingGroupName` - (Required) The name of the autoscaling group.

`AdjustmentType` - (Optional) Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.

`PolicyType` - (Optional) The policy type, either "SimpleScaling", "StepScaling" or "TargetTrackingScaling". If this value isn't provided, AWS will default to "SimpleScaling.".

`EstimatedInstanceWarmup` - (Optional) The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group's specified cooldown period.

`Cooldown` - (Optional) The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.

`ScalingAdjustment` - (Optional) The number of instances by which to scale. `AdjustmentType` determines the interpretation of this number (e.g., as an absolute number or as a percentage of the existing Auto Scaling group size). A positive increment adds to the current capacity and a negative value removes from the current capacity.

`MetricAggregationType` - (Optional) The aggregation type for the policy's metrics. Valid values are "Minimum", "Maximum", and "Average". Without a value, AWS will treat the aggregation type as "Average".

`StepAdjustments` - (Optional) A set of adjustments that manage
group scaling. These have the following structure:.

`ScalingAdjustment` - (Required) The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.

`MetricIntervalLowerBound` - (Optional) The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.

`MetricIntervalUpperBound` - (Optional) The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.

`TargetTrackingConfiguration` - (Optional) A target tracking policy. These have the following structure:.

### TargetTrackingConfiguration Properties

`PredefinedMetricSpecification` - (Optional) A predefined metric. Conflicts with `CustomizedMetricSpecification`.

`CustomizedMetricSpecification` - (Optional) A customized metric. Conflicts with `PredefinedMetricSpecification`.

`TargetValue` - (Required) The target value for the metric.

`DisableScaleIn` - (Optional, Default: false) Indicates whether scale in by the target tracking policy is disabled.


## See Also

* [aws_autoscaling_policy](https://www.terraform.io/docs/providers/aws/r/autoscaling_policy.html) in the _Terraform Provider Documentation_
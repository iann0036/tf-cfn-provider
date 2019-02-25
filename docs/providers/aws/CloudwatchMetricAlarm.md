# Terraform::AWS::CloudwatchMetricAlarm

Provides a CloudWatch Metric Alarm resource.

## Properties

`AlarmName` - (Required) The descriptive name for the alarm. This name must be unique within the user's AWS account.

`Arn` - The ARN of the cloudwatch metric alarm.

`ComparisonOperator` - (Required) The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`.

`EvaluationPeriods` - (Required) The number of periods over which data is compared to the specified threshold.

`MetricName` - (Optional) The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

`Namespace` - (Optional) The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

`Period` - (Optional) The period in seconds over which the specified `Statistic` is applied.

`Statistic` - (Optional) The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`.

`Threshold` - (Required) The value against which the specified statistic is compared.

`ActionsEnabled` - (Optional) Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

`AlarmActions` - (Optional) The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Number (ARN).

`AlarmDescription` - (Optional) The description for the alarm.

`DatapointsToAlarm` - (Optional) The number of datapoints that must be breaching to trigger the alarm.

`Dimensions` - (Optional) The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

`InsufficientDataActions` - (Optional) The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Number (ARN).

`OkActions` - (Optional) The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Number (ARN).

`Unit` - (Optional) The unit for the alarm's associated metric.

`ExtendedStatistic` - (Optional) The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

`TreatMissingData` - (Optional) Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

`EvaluateLowSampleCountPercentiles` - (Optional) Used only for alarms
based on percentiles. If you specify `ignore`, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify `evaluate` or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: `ignore`, and `evaluate`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the health check.

## See Also

* [aws_cloudwatch_metric_alarm](https://www.terraform.io/docs/providers/aws/r/cloudwatch_metric_alarm.html) in the _Terraform Provider Documentation_
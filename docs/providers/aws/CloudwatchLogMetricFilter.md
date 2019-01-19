# Terraform::AWS::CloudwatchLogMetricFilter

Provides a CloudWatch Log Metric Filter resource.

## Properties

`Pattern` - (Required) A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html) for extracting metric data out of ingested log events.

`LogGroupName` - (Required) The name of the log group to associate the metric filter with.

`MetricTransformation` - (Required) A block defining collection of information needed to define how metric data gets emitted. See below.

### MetricTransformation Properties

`Name` - (Required) The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`).

`Namespace` - (Required) The destination namespace of the CloudWatch metric.

`Value` - (Required) What to publish to the metric. For example, if you're counting the occurrences of a particular term like "Error", the value will be "1" for each occurrence. If you're counting the bytes transferred the published value will be the value in the log event.

`DefaultValue` - (Optional) The value to emit when a filter pattern does not match a log event.


## Return Values

### Fn::GetAtt

`Id` - The name of the metric filter.

## See Also

* [aws_cloudwatch_log_metric_filter](https://www.terraform.io/docs/providers/aws/r/cloudwatch_log_metric_filter.html) in the _Terraform Provider Documentation_
# Terraform::Datadog::MetricMetadata

Provides a Datadog metric_metadata resource. This can be used to manage a metric's metadata.

## Properties

`Metric` - (Required) The name of the metric.

`Description` - (Optional) A description of the metric.

`ShortName` - (Optional) A short name of the metric.

`Unit` - (Optional) Primary unit of the metric such as 'byte' or 'operation'.

`PerUnit` - (Optional) 'Per' unit of the metric such as 'second' in 'bytes per second'.

`StatsdInterval` - (Optional) If applicable, stasd flush interval in seconds for the metric.


## See Also

* [datadog_metric_metadata](https://www.terraform.io/docs/providers/datadog/r/metric_metadata.html) in the _Terraform Provider Documentation_
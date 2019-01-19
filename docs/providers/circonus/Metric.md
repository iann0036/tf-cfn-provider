# Terraform::Circonus::Metric

The ``Terraform::Circonus::Metric`` resource creates and manages a
single [metric resource](https://login.circonus.com/resources/api/calls/metric)
that will be instantiated only once a referencing `Terraform::Circonus::Check` has been
created.

## Properties

`Active` - (Optional) A boolean indicating if the metric is being filtered out at the `Terraform::Circonus::Check`'s collector(s) or not.

`Name` - (Required) The name of the metric.  A `Name` must be unique within a `Terraform::Circonus::Check` and its meaning is `circonusCheck.type` specific.

`Tags` - (Optional) A list of tags assigned to the metric.

`Type` - (Required) The type of metric.  This value must be present and can be one of the following values: `numeric`, `text`, `histogram`, `composite`, or `caql`.

`Unit` - (Optional) The unit of measurement for this `Terraform::Circonus::Metric`.


## See Also

* [circonus_metric](https://www.terraform.io/docs/providers/circonus/r/metric.html) in the _Terraform Provider Documentation_
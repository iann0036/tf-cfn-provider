# Terraform::Librato::Metric

Provides a Librato Metric resource. This can be used to create and manage metrics on Librato.

## Properties

`Type` - (Required) The type of metric to create (gauge, counter, or composite).

`Name` - (Required) The unique identifier of the metric.

`DisplayName` - The name which will be used for the metric when viewing the Metrics website.

`Description` - Text that can be used to explain precisely what the metric is measuring.

`Period` - Number of seconds that is the standard reporting period of the metric.

`Attributes` - The attributes hash configures specific components of a metric’s visualization.

`Composite` - The definition of the composite metric.


## Return Values

### Fn::GetAtt

`Name` - The identifier for the metric.

`DisplayName` - The name which will be used for the metric when viewing the Metrics website.

`Type` - The type of metric to create (gauge, counter, or composite).

`Description` - Text that describes precisely what the metric is measuring.

`Period` - Number of seconds that is the standard reporting period of the metric. Setting the period enables Metrics to detect abnormal interruptions in reporting and aids in analytics. For gauge metrics that have service-side aggregation enabled, this option will define the period that aggregation occurs on.

`Composite` - The composite definition. Only used when type is composite.

`Color` - Sets a default color to prefer when visually rendering the metric. Must be a seven character string that represents the hex code of the color e.g. #52D74C.

`DisplayMax` - If a metric has a known theoretical maximum value, set display_max so that visualizations can provide perspective of the current values relative to the maximum value.

`DisplayMin` - If a metric has a known theoretical minimum value, set display_min so that visualizations can provide perspective of the current values relative to the minimum value.

`DisplayUnitsLong` - A string that identifies the unit of measurement e.g. Microseconds. Typically the long form of display_units_short and used in visualizations e.g. the Y-axis label on a graph.

`Aggregate` - Enable service-side aggregation for this metric. When enabled, measurements sent using the same tag set will be aggregated into single measurements on an interval defined by the period of the metric. If there is no period defined for the metric then all measurements will be aggregated on a 60-second interval.

## See Also

* [librato_metric](https://www.terraform.io/docs/providers/librato/r/metric.html) in the _Terraform Provider Documentation_
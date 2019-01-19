# Terraform::Librato::SpaceChart

Provides a Librato Space Chart resource. This can be used to
create and manage charts in Librato Spaces.

## Properties

`SpaceId` - (Required) The ID of the space this chart should be in.

`Name` - (Required) The title of the chart when it is displayed.

`Type` - (Optional) Indicates the type of chart. Must be one of line or stacked (default to line).

`Min` - (Optional) The minimum display value of the chart's Y-axis.

`Max` - (Optional) The maximum display value of the chart's Y-axis.

`Label` - (Optional) The Y-axis label.

`RelatedSpace` - (Optional) The ID of another space to which this chart is related.

`Stream` - (Optional) Nested block describing a metric to use for data in the chart. The structure of this block is described below.

### Stream Properties

`Metric` - (Required) The name of the metric. May not be specified if `Composite` is specified.

`Source` - (Required) The name of a source, or `*` to include all sources. This field will also accept specific wildcard entries. For example us-west-\*-app will match us-west-21-app but not us-west-12-db. Use % to specify a dynamic source that will be provided after the instrument or dashboard has loaded, or in the URL. May not be specified if `Composite` is specified.

`GroupFunction` - (Required) How to process the results when multiple sources will be returned. Value must be one of average, sum, breakout. If average or sum, a single line will be drawn representing the average or sum (respectively) of all sources. If the group_function is breakout, a separate line will be drawn for each source. If this property is not supplied, the behavior will default to average. May not be specified if `Composite` is specified.

`Composite` - (Required) A composite metric query string to execute when this stream is displayed. May not be specified if `Metric`, `Source` or `GroupFunction` is specified.

`SummaryFunction` - (Optional) When visualizing complex measurements or a rolled-up measurement, this allows you to choose which statistic to use. Defaults to "average". Valid options are: "max", "min", "average", "sum" or "count".

`Name` - (Optional) A display name to use for the stream when generating the tooltip.

`Color` - (Optional) Sets a color to use when rendering the stream. Must be a seven character string that represents the hex code of the color e.g. "#52D74C".

`UnitsShort` - (Optional) Unit value string to use as the tooltip label.

`UnitsLong` - (Optional) String value to set as they Y-axis label. All streams that share the same units_long value will be plotted on the same Y-axis.

`Min` - (Optional) Theoretical minimum Y-axis value.

`Max` - (Optional) Theoretical maximum Y-axis value.

`TransformFunction` - (Optional) Linear formula to run on each measurement prior to visualization.

`Period` - (Optional) An integer value of seconds that defines the period this stream reports at. This aids in the display of the stream and allows the period to be used in stream display transforms.


## Return Values

### Fn::GetAtt

`Id` - The ID of the chart.

`SpaceId` - The ID of the space this chart should be in.

`Title` - The title of the chart when it is displayed.

## See Also

* [librato_space_chart](https://www.terraform.io/docs/providers/librato/r/space_chart.html) in the _Terraform Provider Documentation_
# Terraform::Circonus::Graph

The ``Terraform::Circonus::Graph`` resource creates and manages a
[Circonus Graph](https://login.circonus.com/user/docs/Visualization/Graph/Create).

https://login.circonus.com/resources/api/calls/graph).

## Properties

`Description` - (Optional) Description of what the graph is for.

`GraphStyle` - (Optional) How the graph should be rendered.  Valid options are `area` or `line` (default).

`Left` - (Optional) A map of graph left axis options.  Valid values in `Left` include: `logarithmic` can be set to `0` (default) or `1`; `min` is the `min` Y axis value on the left; and `max` is the Y axis max value on the left.

`LineStyle` - (Optional) How the line should change between points.  Can be either `stepped` (default) or `interpolated`.

`Name` - (Required) The title of the graph.

`Notes` - (Optional) A place for storing notes about this graph.

`Right` - (Optional) A map of graph right axis options.  Valid values in `Right` include: `logarithmic` can be set to `0` (default) or `1`; `min` is the `min` Y axis value on the right; and `max` is the Y axis max value on the right.

`Metric` - (Optional) A list of metric streams to graph.  See below for options.

`MetricCluster` - (Optional) A metric cluster to graph.  See below for options.

`Tags` - (Optional) A list of tags assigned to this graph.


## See Also

* [circonus_graph](https://www.terraform.io/docs/providers/circonus/r/graph.html) in the _Terraform Provider Documentation_
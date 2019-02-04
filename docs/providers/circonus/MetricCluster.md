# Terraform::Circonus::MetricCluster

The ``Terraform::Circonus::MetricCluster`` resource creates and manages a
[Circonus Metric Cluster](https://login.circonus.com/user/docs/Data/View/MetricClusters).

## Properties

`Description` - (Optional) A long-form description of the metric cluster.

`Name` - (Required) The name of the metric cluster.  This name must be unique
across all metric clusters in a given Circonus Account.

`Query` - (Required) One or more `Query` attributes must be present.  Each
`Query` must contain both a `definition` and a `type`.  See below for details
on supported attributes.

`Tags` - (Optional) A list of tags attached to the metric cluster.


## See Also

* [circonus_metric_cluster](https://www.terraform.io/docs/providers/circonus/r/metric_cluster.html) in the _Terraform Provider Documentation_
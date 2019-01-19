# Terraform::Google::DataprocCluster

Manages a Cloud Dataproc cluster resource within GCP. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).


!> **Warning:** Due to limitations of the API, all arguments except
`labels`,`cluster_config.worker_config.num_instances` and `cluster_config.preemptible_worker_config.num_instances` are non-updateable. Changing others will cause recreation of the
whole cluster!

## Properties

TBC

## Return Values

### Fn::GetAtt

`ClusterConfig.masterConfig.instanceNames` - List of master instance names which.

`ClusterConfig.workerConfig.instanceNames` - List of worker instance names which have been assigned.

`ClusterConfig.preemptibleWorkerConfig.instanceNames` - List of preemptible instance names which have been assigned.

`ClusterConfig.bucket` - The name of the cloud storage bucket ultimately used to house the staging data.

`ClusterConfig.softwareConfig.properties` - A list of the properties used to set the daemon config files.

## See Also

* [google_dataproc_cluster](https://www.terraform.io/docs/providers/google/r/dataproc_cluster.html) in the _Terraform Provider Documentation_
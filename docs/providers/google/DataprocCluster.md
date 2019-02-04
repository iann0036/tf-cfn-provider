# Terraform::Google::DataprocCluster

Manages a Cloud Dataproc cluster resource within GCP. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).


!> **Warning:** Due to limitations of the API, all arguments except
`Labels`,`cluster_config.worker_config.num_instances` and `cluster_config.preemptible_worker_config.num_instances` are non-updateable. Changing others will cause recreation of the
whole cluster!

## Properties

`Name` - (Required) The name of the cluster, unique within the project and
zone.

`Project` - (Optional) The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.

`Region` - (Optional) The region in which the cluster and associated nodes will be created in.
Defaults to `global`.

`Labels` - (Optional, Computed) The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.

`ClusterConfig` - (Optional) Allows you to configure various aspects of the cluster.
Structure defined below.

### ClusterConfig Properties

`StagingBucket` - (Optional) The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don't explicitly specify a `StagingBucket`
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.

`Zone` - (Optional, Computed) The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If `Region` is set to 'global' (default)
then `Zone` is mandatory, otherwise GCP is able to make use of [Auto Zone Placement](https://cloud.google.com/dataproc/docs/concepts/auto-zone)
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
`cluster_config.master_config.machine_type` and `cluster_config.worker_config.machine_type`.

`Network` - (Optional, Computed) The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with `Subnetwork`.
If neither is specified, this defaults to the "default" network.

`Subnetwork` - (Optional) The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with `Network`.

`ServiceAccount` - (Optional) The service account to be used by the Node VMs.
If not specified, the "default" service account is used.

`ServiceAccountScopes` - (Optional, Computed) The set of Google API scopes to be made available
on all of the node VMs under the `ServiceAccount` specified. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:.

`Tags` - (Optional) The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.

`InternalIpOnly` - (Optional) By default, clusters are not restricted to internal IP addresses,
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as `privateIpGoogleAccess`) must be enabled on the subnetwork that the cluster
will be launched in.

`Metadata` - (Optional) A map of the Compute Engine metadata entries to add to all instances
(see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)).

`NumInstances` - (Optional, Computed) Specifies the number of master nodes to create.
If not specified, GCP will default to a predetermined computed value (currently 1).

`MachineType` - (Optional, Computed) The name of a Google Compute Engine machine type
to create for the master. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).

`BootDiskType` - (Optional) The disk type of the primary disk attached to each node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.

`BootDiskSizeGb` - (Optional, Computed) Size of the primary disk attached to each node, specified
in GB. The primary disk contains the boot volume and system libraries, and the
smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.

`NumLocalSsds` - (Optional) The amount of local SSD disks that will be
attached to each master cluster node. Defaults to 0.

`AcceleratorType` - (Required) The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.

`AcceleratorCount` - (Required) The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.

`NumInstances` - (Optional, Computed) Specifies the number of worker nodes to create.
If not specified, GCP will default to a predetermined computed value (currently 2).
There is currently a beta feature which allows you to run a
[Single Node Cluster](https://cloud.google.com/dataproc/docs/concepts/single-node-clusters).
In order to take advantage of this you need to set
`"dataproc:dataproc.allow.zero.workers" = "true"` in
`cluster_config.software_config.properties`.

`MachineType` - (Optional, Computed) The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).

`BootDiskType` - (Optional) The disk type of the primary disk attached to each node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.

`BootDiskSizeGb` - (Optional, Computed) Size of the primary disk attached to each worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.

`NumLocalSsds` - (Optional) The amount of local SSD disks that will be
attached to each worker cluster node. Defaults to 0.

`AcceleratorType` - (Required) The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.

`AcceleratorCount` - (Required) The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.

`NumInstances` - (Optional) Specifies the number of preemptible nodes to create.
Defaults to 0.

`BootDiskType` - (Optional) The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.

`BootDiskSizeGb` - (Optional, Computed) Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.

`NumLocalSsds` - (Optional) The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.

`ImageVersion` - (Optional, Computed) The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
[Cloud Dataproc versions](https://cloud.google.com/dataproc/docs/concepts/dataproc-versions).

`OverrideProperties` - (Optional) A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
[Cluster properties](https://cloud.google.com/dataproc/docs/concepts/cluster-properties).

### InitializationAction Properties

`Script` - (Required) The script to be executed during initialization of the cluster.
The script must be a GCS file with a gs:// prefix.

`TimeoutSec` - (Optional, Computed) The maximum duration (in seconds) which `Script` is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).

### EncryptionConfig Properties

`KmsKeyName` - (Required) The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.


## Return Values

### Fn::GetAtt

`ClusterConfig.masterConfig.instanceNames` - List of master instance names which.

`ClusterConfig.workerConfig.instanceNames` - List of worker instance names which have been assigned.

`ClusterConfig.preemptibleWorkerConfig.instanceNames` - List of preemptible instance names which have been assigned.

`ClusterConfig.bucket` - The name of the cloud storage bucket ultimately used to house the staging data.

`ClusterConfig.softwareConfig.properties` - A list of the properties used to set the daemon config files.

## See Also

* [google_dataproc_cluster](https://www.terraform.io/docs/providers/google/r/dataproc_cluster.html) in the _Terraform Provider Documentation_
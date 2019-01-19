# Terraform::Spotinst::ElastigroupGke

Provides a Spotinst elastigroup GKE resource.

## Properties

`Name` - (Optional) The group name.

`MaxSize` - (Required) The maximum number of instances the group should have at any time.

`MinSize` - (Required) The minimum number of instances the group should have at any time.

`DesiredCapacity` - (Required) The desired number of instances the group should have at any time.

`AvailabilityZones` - (Optional) List of availability zones for the group.

`ClusterZoneName` - (Required) The zone where the cluster is hosted.

`ClusterId` - (Required) The name of the GKE cluster you wish to import.

`NodeImage` - (Optional, Default: `COS`) The image that will be used for the node VMs. Possible values: COS, UBUNTU.

`PreemptiblePercentage` - (Optional) The percentage of preemptible VMs that would spin up from the desired capacity (range: 0-100).

`InstanceTypesPreemptible` - (Optional) The preemptible VMs instance type. To maximize cost savings and market availability, select as many types as possible. Required if instance_types_on_demand is not set.

`InstanceTypesOnDemand` - (Optional) The regular VM instance type to use for mixed-type groups and when falling back to on-demand. Required if instance_types_preemptible is not set.


## See Also

* [spotinst_elastigroup_gke](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gke.html) in the _Terraform Provider Documentation_
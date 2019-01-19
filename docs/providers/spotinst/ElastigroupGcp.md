# Terraform::Spotinst::ElastigroupGcp

Provides a Spotinst elastigroup GCP resource.

## Properties

`Name` - (Required) The group name.

`Description` - (Optional) The region your GCP group will be created in.

`StartupScript` - (Optional) Create and run your own startup scripts on your virtual machines to perform automated tasks every time your instance boots up.

`ServiceAccount` - (Optional) The email of the service account in which the group instances will be launched.

`MaxSize` - (Required) The maximum number of instances the group should have at any time.

`MinSize` - (Required) The minimum number of instances the group should have at any time.

`DesiredCapacity` - (Required) The desired number of instances the group should have at any time.

`AvailabilityZones` - (Required) List of availability zones for the group.

`Subnets` - (Optional) A list of regions and subnets.

`Region` - (Required) The region for the group of subnets.

`SubnetNames` - (Required) The names of the subnets in the region.

`InstanceTypesPreemptible` - (Required) The preemptible VMs instance type. To maximize cost savings and market availability, select as many types as possible. Required if instance_types_on_demand is not set.

`InstanceTypesOnDemand` - (Required) The regular VM instance type to use for mixed-type groups and when falling back to on-demand. Required if instance_types_preemptible is not set.

`InstanceTypesCustom` - (Required) Defines a set of custom instance types. Required if instance_types_preemptible and instance_types_on_demand are not set.

`VCPU` - (Optional) The number of vCPUs in the custom instance type. GCP has a number of limitations on accepted vCPU values. For more information, see the GCP documentation (here.)[https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications].

`MemoryGib` - (Optional) The memory (in GiB) in the custom instance types. GCP has a number of limitations on accepted memory values.For more information, see the GCP documentation (here.)[https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications].

`PreemptiblePercentage` - (Optional) Percentage of Preemptible VMs to spin up from the "desired_capacity".

`OnDemandCount` - (Optional) Number of regular VMs to launch in the group. The rest will be Preemptible VMs. When this parameter is specified, the preemptible_percentage parameter is being ignored.

`FallbackToOd` - (Optional) Activate fallback-to-on-demand. When provisioning an instance, if no Preemptible market is available, fallback-to-on-demand will provision an On-Demand instance to maintain the group capacity.

`DrainingTimeout` - (Optional) Time (seconds) the instance is allowed to run after it is detached from the group. This is to allow the instance time to drain all the current TCP connections before terminating it.

`Gpu` - (Optional) Defines the GPU configuration.

`Type` - (Required) The type of GPU instance. Valid values: `nvidia-tesla-v100`, `nvidia-tesla-p100`, `nvidia-tesla-k80`.

`Count` - (Required) The number of GPUs. Must be 0, 2, 4, 6, 8.

`HealthCheckGracePeriod` - (optional) Period of time (seconds) to wait for VM to reach healthiness before monitoring for unhealthiness.

`NetworkInterface` - (Required, minimum 1) Array of objects representing the network configuration for the elastigroup.

`Network` - (Required) Network resource for this group.

`AccessConfigs` - (Optional) Array of configurations.

`Name` - (Optional) Name of this access configuration.

`Type` - (Optional) Array of configurations for this interface. Currently, only ONE_TO_ONE_NAT is supported.

`Tags` - (Optional) Tags to mark created instances.

`BackendServices` - (Optional) Describes the backend service configurations.

`ServiceName` - (Required).

`NamedPort` - (Optional) Describes a named port and a list of ports.

`PortName` - (Required) The name of the port.

`Ports` - (Required) A list of ports.

`Metadata` - (Optional) Array of objects with key-value pairs.

`Key` - (Optional) Metadata key.

`Value` - (Optional) Metadata value.

`Labels` - (Optional) Array of objects with key-value pairs.

`Key` - (Optional) Labels key.

`Value` - (Optional) Labels value.

`Disks` - (Optional) Array of disks associated with this instance. Persistent disks must be created before you can assign them.

`AutoDelete` - (Optional) Specifies whether the disk will be auto-deleted when the instance is deleted.

`Boot` - (Optional) Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.

`DeviceName` - (Optional) Specifies a unique device name of your choice.

`Interface` - (Optional, Default: `SCSI`) Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME.

`Mode` - (Optional, Default: `READ_WRITE`) The mode in which to attach this disk, either READ_WRITE or READ_ONLY.

`Source` - (Optional) Specifies a valid partial or full URL to an existing Persistent Disk resource. This field is only applicable for persistent disks.

`Type` - (Optional, Default: `PERSISTENT`) Specifies the type of disk, either SCRATCH or PERSISTENT.

`InitializeParams` - (Optional) Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.

`DiskSizeGb` - (Optional) Specifies disk size in gigabytes. Must be in increments of 2.

`DiskType` - (Optional, Default" `pd-standard`) Specifies the disk type to use to create the instance. Valid values: pd-ssd, local-ssd.

`SourceImage` - (Optional) A source image used to create the disk. You can provide a private (custom) image, and Compute Engine will use the corresponding image from your project.

`ScalingUpPolicy` - (Optional) Contains scaling policies for scaling the Elastigroup up.

`ScalingDownPolicy` - (Optional) Contains scaling policies for scaling the Elastigroup down.

`PolicyName` - (Optional) Name of scaling policy.

`MetricName` - (Optional) Metric to monitor. Valid values: "Percentage CPU", "Network In", "Network Out", "Disk Read Bytes", "Disk Write Bytes", "Disk Write Operations/Sec", "Disk Read Operations/Sec".

`Statistic` - (Optional) Statistic by which to evaluate the selected metric. Valid values: "AVERAGE", "SAMPLE_COUNT", "SUM", "MINIMUM", "MAXIMUM", "PERCENTILE", "COUNT".

`Threshold` - (Optional) The value at which the scaling action is triggered.

`Period` - (Optional) Amount of time (seconds) for which the threshold must be met in order to trigger the scaling action.

`EvaluationPeriods` - (Optional) Number of consecutive periods in which the threshold must be met in order to trigger a scaling action.

`Cooldown` - (Optional) Time (seconds) to wait after a scaling action before resuming monitoring.

`Operator` - (Optional) The operator used to evaluate the threshold against the current metric value. Valid values: "gt" (greater than), "get" (greater-than or equal), "lt" (less than), "lte" (less than or equal).

`Action` - (Optional) Scaling action to take when the policy is triggered.

`Type` - (Optional) Type of scaling action to take when the scaling policy is triggered. Valid values: "adjustment", "setMinTarget", "updateCapacity", "percentageAdjustment".

`Adjustment` - (Optional) Value to which the action type will be adjusted. Required if using "numeric" or "percentageAdjustment" action types.


## See Also

* [spotinst_elastigroup_gcp](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_gcp.html) in the _Terraform Provider Documentation_
# Terraform::Google::ComputeRegionInstanceGroupManager

The Google Compute Engine Regional Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)
and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers)

~> **Note:** Use [google_compute_instance_group_manager](/docs/providers/google/r/compute_instance_group_manager.html) to create a single-zone instance group manager.

## Properties

`BaseInstanceName` - (Required) The base instance name to use for instances in this group. The value must be a valid [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters are lowercase letters, numbers, and hyphens (-). Instances are named by appending a hyphen and a random four-character string to the base instance name.

`InstanceTemplate` - (Optional) The full URL to an instance template from which all new instances will be created. This field is only present in the `google` provider.

`Version` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) Application versions managed by this instance group. Each version deals with a specific instance template, allowing canary release scenarios. Structure is documented below.

`Name` - (Required) The name of the instance group manager. Must be 1-63 characters long and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Supported characters include lowercase letters, numbers, and hyphens.

`Region` - (Required) The region where the managed instance group resides.

`Description` - (Optional) An optional textual description of the instance group manager.

`NamedPort` - (Optional) The named port configuration. See the section below for details on configuration.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`TargetSize` - (Optional) The target number of running instances for this managed instance group. This value should always be explicitly set unless this resource is attached to an autoscaler, in which case it should never be set. Defaults to `0`.

`TargetPools` - (Optional) The full URL of all target pools to which new instances in the group are added. Updating the target pools attribute does not affect existing instances.

`WaitForInstances` - (Optional) Whether to wait for all instances to be created/updated before returning. Note that if this is set to true and the operation does not succeed, Terraform will continue trying until it times out.

`AutoHealingPolicies` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) The autohealing policies for this managed instance group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).

`UpdatePolicy` - (Optional, [Beta](https://terraform.io/docs/providers/google/provider_versions.html)) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch).

`DistributionPolicyZones` - (Optional) The distribution policy for this managed instance group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones). - - -.

### UpdatePolicy Properties

`MinimalAction` - (Required) - Minimal action to be taken on an instance. Valid values are `"RESTART"`, `"REPLACE"`.

`Type` - (Required) - The type of update. Valid values are `"OPPORTUNISTIC"`, `"PROACTIVE"`.

`MaxSurgeFixed` - (Optional), The maximum number of instances that can be created above the specified targetSize during the update process. Conflicts with `MaxSurgePercent`. It has to be either 0 or at least equal to the number of zones.  If fixed values are used, at least one of `MaxUnavailableFixed` or `MaxSurgeFixed` must be greater than 0.

`MaxSurgePercent` - (Optional), The maximum number of instances(calculated as percentage) that can be created above the specified targetSize during the update process. Conflicts with `MaxSurgeFixed`. Percent value is only allowed for regional managed instance groups with size at least 10.

`MaxUnavailableFixed` - (Optional), The maximum number of instances that can be unavailable during the update process. Conflicts with `MaxUnavailablePercent`. It has to be either 0 or at least equal to the number of zones. If fixed values are used, at least one of `MaxUnavailableFixed` or `MaxSurgeFixed` must be greater than 0.

`MaxUnavailablePercent` - (Optional), The maximum number of instances(calculated as percentage) that can be unavailable during the update process. Conflicts with `MaxUnavailableFixed`. Percent value is only allowed for regional managed instance groups with size at least 10.

`MinReadySec` - (Optional), Minimum number of seconds to wait for after a newly created instance becomes available. This value must be from range [0, 3600] - - -.

`Name` - (Required) The name of the port.

`Port` - (Required) The port number. - - -.

### AutoHealingPolicies Properties

`HealthCheck` - (Required) The health check resource that signals autohealing.

`InitialDelaySec` - (Required) The number of seconds that the managed instance group waits before it applies autohealing policies to new instances or recently recreated instances. Between 0 and 3600.

### Version Properties

`Name` - (Required) - Version name.

`InstanceTemplate` - (Required) - The full URL to an instance template from which all new instances of this version will be created.

`TargetSize` - (Optional) - The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.

### TargetSize Properties

`Fixed` - (Optional), The number of instances which are managed for this version. Conflicts with `Percent`.

`Percent` - (Optional), The number of instances (calculated as percentage) which are managed for this version. Conflicts with `Fixed`. Note that when using `Percent`, rounding will be in favor of explicitly set `TargetSize` values; a managed instance group with 2 instances and 2 `Version`s, one of which has a `target_size.percent` of `60` will create 2 instances of that `Version`.


## Return Values

### Fn::GetAtt

`Fingerprint` - The fingerprint of the instance group manager.

`InstanceGroup` - The full URL of the instance group created by the manager.

`SelfLink` - The URL of the created resource.

## See Also

* [google_compute_region_instance_group_manager](https://www.terraform.io/docs/providers/google/r/compute_region_instance_group_manager.html) in the _Terraform Provider Documentation_
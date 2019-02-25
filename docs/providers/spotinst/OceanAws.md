# Terraform::Spotinst::OceanAws

Provides a Spotinst Ocean AWS resource.

## Properties

`Name` - (Required) The cluster name.

`ControllerId` - (Required) The ocean cluster identifier. Example: `ocean.k8s`.

`Region` - (Required) The region the cluster will run in.

`MaxSize` - (Optional, Default: `1000`) The upper limit of instances the cluster can scale up to.

`MinSize` - (Optional) The lower limit of instances the cluster can scale down to.

`DesiredCapacity` - (Optional) The number of instances to launch and maintain in the cluster.

`SubnetIds` - (Required) A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.

`Whitelist` - (Optional) Instance types allowed in the Ocean cluster. Cannot be configured if `Blacklist` is configured.

`Blacklist` - (Optional) Instance types not allowed in the Ocean cluster. Cannot be configured if `Whitelist` is configured.

`UserData` - (Optional) Base64-encoded MIME user data to make available to the instances.

`ImageId` - (Required) ID of the image used to launch the instances.

`SecurityGroups` - (Required) One or more security group ids.

`KeyName` - (Optional) The key pair to attach the instances.

`IamInstanceProfile` - (Optional) The instance profile iam role.

`AssociatePublicIpAddress` - (Optional).

`LoadBalancers` - (Optional) - Array of load balancer objects to add to ocean cluster
* `Arn` - (Optional) Required if type is set to TARGET_GROUP
* `Name` - (Optional) Required if type is set to CLASSIC
* `Type` - (Required) Can be set to CLASSIC or TARGET_GROUP.

`Arn` - (Optional) Required if type is set to TARGET_GROUP
* `Name` - (Optional) Required if type is set to CLASSIC
* `Type` - (Required) Can be set to CLASSIC or TARGET_GROUP.

`Name` - (Optional) Required if type is set to CLASSIC
* `Type` - (Required) Can be set to CLASSIC or TARGET_GROUP.

`Type` - (Required) Can be set to CLASSIC or TARGET_GROUP.

`FallbackToOndemand` - (Optional, Default: `true`) If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.

`SpotPercentage` - (Optional, Default: `100`) The percentage of Spot instances the cluster should maintain. Min 0, max 100.

`UtilizeReservedInstances` - (Optional, Default `false`) If Reserved instances exist, OCean will utilize them before launching Spot instances.

`Autoscaler` - (Optional) Describes the Ocean Kubernetes autoscaler.

`AutoscaleIsEnabled` - (Optional, Default: `true`) Enable the Ocean Kubernetes autoscaler.

`AutoscaleIsAutoConfig` - (Optional, Default: `true`) Automatically configure and optimize headroom resources.

`AutoscaleCooldown` - (Optional, Default: `null`) Cooldown period between scaling actions.

`AutoscaleHeadroom` - (Optional) Spare resource capacity management enabling fast assignment of Pods without waiting for new resources to launch.

`CpuPerUnit` - (Optional) Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.

`GpuPerUnit` - (Optional) Optionally configure the number of GPUS to allocate the headroom.

`MemoryPerUnit` - (Optional) Optionally configure the amount of memory (MB) to allocate the headroom.

`NumOfUnits` - (Optional) The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.

`AutoscaleDown` - (Optional) Auto Scaling scale down operations.

`EvaluationPeriods` - (Optional, Default: `null`) The number of evaluation periods that should accumulate before a scale down action takes place.

`ResourceLimits` - (Optional) Optionally set upper and lower bounds on the resource usage of the cluster.

`MaxVcpu` - (Optional) The maximum cpu in vCPU units that can be allocated to the cluster.

`MaxMemoryGib` - (Optional) The maximum memory in GiB units that can be allocated to the cluster.

`Tags` - (Optional) Optionally adds tags to instances launched in an Ocean cluster.

`TagKey` - (Optional) The tag key.

`TagValue` - (Optional) The tag value.


## See Also

* [spotinst_ocean_aws](https://www.terraform.io/docs/providers/spotinst/r/ocean_aws.html) in the _Terraform Provider Documentation_
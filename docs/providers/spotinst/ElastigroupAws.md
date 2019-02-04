# Terraform::Spotinst::ElastigroupAws

Provides a Spotinst AWS group resource.

## Properties

`Name` - (Required) The group name.

`Description` - (Optional) The group description.

`Product` - (Required) Operation system type. Valid values: `"Linux/UNIX"`, `"SUSE Linux"`, `"Windows"`.
For EC2 Classic instances:  `"Linux/UNIX (Amazon VPC)"`, `"SUSE Linux (Amazon VPC)"`, `"Windows (Amazon VPC)"`.

`AvailabilityZones` - (Optional) List of Strings of availability zones.
Note: When this parameter is set, `SubnetIds` should be left unused.

`SubnetIds` - (Optional) List of Strings of subnet identifiers.
Note: When this parameter is set, `AvailabilityZones` should be left unused.

`Region` - (Optional) The AWS region your group will be created in.
Note: This parameter is required if you specify subnets (through subnet_ids). This parameter is optional if you specify Availability Zones (through availability_zones).

`PreferredAvailabilityZones` - The AZs to prioritize when launching Spot instances. If no markets are available in the Preferred AZs, Spot instances are launched in the non-preferred AZs.
Note: Must be a sublist of `AvailabilityZones` and `Orientation` value must not be `"equalAzDistribution"`.

`MaxSize` - (Optional; Required if using scaling policies) The maximum number of instances the group should have at any time.

`MinSize` - (Optional; Required if using scaling policies) The minimum number of instances the group should have at any time.

`DesiredCapacity` - (Optional) The desired number of instances the group should have at any time.

`CapacityUnit` - (Optional, Default: `"instance"`) The capacity unit to launch instances by. If not specified, when choosing the weight unit, each instance will weight as the number of its vCPUs.

`SecurityGroups` - (Required) A list of associated security group IDS.

`ImageId` - (Optional) The ID of the AMI used to launch the instance.

`IamInstanceProfile` - (Optional) The ARN or name of an IAM instance profile to associate with launched instances.

`KeyName` - (Optional) The key name that should be used for the instance.

`EnableMonitoring` - (Optional) Indicates whether monitoring is enabled for the instance.

`UserData` - (Optional) The user data to provide when launching the instance.

`ShutdownScript` - (Optional) The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: [Shutdown Script](https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/).

`EbsOptimized` - (Optional) Enable high bandwidth connectivity between instances and AWS’s Elastic Block Store (EBS). For instance types that are EBS-optimized by default this parameter will be ignored.

`PlacementTenancy` - (Optional) Enable dedicated tenancy. Note: There is a flat hourly fee for each region in which dedicated tenancy is used.

`InstanceTypesOndemand` - (Required) The type of instance determines your instance's CPU capacity, memory and storage (e.g., m1.small, c1.xlarge).

`InstanceTypesSpot` - (Required) One or more instance types.

`InstanceTypesPreferredSpot` - (Optional) Prioritize a subset of spot instance types. Must be a subset of the selected spot instance types.

`InstanceTypesWeights` - (Optional) List of weights per instance type for weighted groups. Each object in the list should have the following attributes:.

`Weight` - (Required) Weight per instance type (Integer).

`InstanceType` - (Required) Name of instance type (String).

`CpuCredits` - (Optional) Controls how T3 instances are launched. Valid values: `standard`, `unlimited`.

`FallbackToOndemand` - (Required) In a case of no Spot instances available, Elastigroup will launch on-demand instances instead.

`WaitForCapacity` - (Optional) Minimum number of instances in a 'HEALTHY' status that is required before continuing. This is ignored when updating with blue/green deployment. Cannot exceed `DesiredCapacity`.

`WaitForCapacityTimeout` - (Optional) Time (seconds) to wait for instances to report a 'HEALTHY' status. Useful for plans with multiple dependencies that take some time to initialize. Leave undefined or set to `0` to indicate no wait. This is ignored when updating with blue/green deployment.

`Orientation` - (Required, Default: `"balanced"`) Select a prediction strategy. Valid values: `"balanced"`, `"costOriented"`, `"equalAzDistribution"`, `"availabilityOriented"`.

`SpotPercentage` - (Optional; Required if not using `OndemandCount`) The percentage of Spot instances that would spin up from the `DesiredCapacity` number.

`OndemandCount` - (Optional; Required if not using `SpotPercentage`) Number of on demand instances to launch in the group. All other instances will be spot instances. When this parameter is set the `SpotPercentage` parameter is being ignored.

`DrainingTimeout` - (Optional) The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.

`UtilizeReservedInstances` - (Optional) In a case of any available reserved instances, Elastigroup will utilize them first before purchasing Spot instances.

`HealthCheckType` - (Optional) The service that will perform health checks for the instance. Valid values: `"ELB"`, `"HCS"`, `"TARGET_GROUP"`, `"MLB"`, `"EC2"`, `"MULTAI_TARGET_SET"`, `"MLB_RUNTIME"`, `"K8S_NODE"`, `"NOMAD_NODE"`, `"ECS_CLUSTER_INSTANCE"`.

`HealthCheckGracePeriod` - (Optional) The amount of time, in seconds, after the instance has launched to starts and check its health.

`HealthCheckUnhealthyDurationBeforeReplacement` - (Optional) The amount of time, in seconds, that we will wait before replacing an instance that is running and became unhealthy (this is only applicable for instances that were once healthy).

`Tags` - (Optional) A key/value mapping of tags to assign to the resource.

`ElasticIps` - (Optional) A list of [AWS Elastic IP](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) allocation IDs to associate to the group instances.

`RevertToSpot` - (Optional) Hold settings for strategy correction – replacing On-Demand for Spot instances. Supported Values: `"never"`, `"always"`, `"timeWindow"`.

`PerformAt` - (Required) In the event of a fallback to On-Demand instances, select the time period to revert back to Spot. Supported Arguments – always (default), timeWindow, never. For timeWindow or never to be valid the group must have availabilityOriented OR persistence defined.

`TimeWindows` - (Optional) Specify a list of time windows for to execute revertToSpot strategy. Time window format: `ddd:hh:mm-ddd:hh:mm`. Example: `Mon:03:00-Wed:02:30`.


## Return Values

### Fn::GetAtt

`Id` - The group ID.

## See Also

* [spotinst_elastigroup_aws](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws.html) in the _Terraform Provider Documentation_
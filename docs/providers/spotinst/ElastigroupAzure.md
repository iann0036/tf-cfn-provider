# Terraform::Spotinst::ElastigroupAzure

Provides a Spotinst elastigroup Azure resource.

## Properties

`Name` - (Required) The group name.

`Region` - (Required) The region your Azure group will be created in.

`ResourceGroupName` - (Required) Vnet Resource Group Name.

`Product` - (Required) Operation system type. Valid values: `"Linux"`, `"Windows"`.

`MaxSize` - (Required) The maximum number of instances the group should have at any time.

`MinSize` - (Required) The minimum number of instances the group should have at any time.

`DesiredCapacity` - (Required) The desired number of instances the group should have at any time.

`OdSizes` - (Required) Available On-Demand sizes.

`LowPrioritySizes` - (Required) Available Low-Priority sizes.

`Strategy` - (Required) Describes the deployment strategy.

`LowPriorityPercentage` - (Optional, Default `100`) Percentage of Low Priority instances to maintain. Required if `OdCount` is not specified.

`OdCount` - (Optional) Number of On-Demand instances to maintain. Required if low_priority_percentage is not specified.

`DrainingTimeout` - (Optional, Default `120`) Time (seconds) to allow the instance to be drained from incoming TCP connections and detached from MLB before terminating it during a scale-down operation.

`LoadBalancers` - (Required) Describes a set of one or more classic load balancer target groups and/or Multai load balancer target sets.

`Type` - (Required) The resource type. Valid values: CLASSIC, TARGET_GROUP, MULTAI_TARGET_SET.

`BalancerId` - (Required) The balancer ID.

`TargetSetId` - (Required) The scale set ID associated with the load balancer.

`AutoWeight` - (Optional, Default: `false`).

`Image` - (Required) Image of a VM. An image is a template for creating new VMs. Choose from Azure image catalogue (marketplace) or use a custom image.

`Publisher` - (Optional) Image publisher. Required if resource_group_name is not specified.

`Offer` - (Optional) Name of the image to use. Required if publisher is specified.

`UserData` - (Optional) Base64-encoded MIME user data to make available to the instances.

`Sku` - (Optional) Image's Stock Keeping Unit, which is the specific version of the image. Required if publisher is specified.

`ImageName` - (Optional) Name of the custom image. Required if resource_group_name is specified.

`HealthCheck` - (Optional) Describes the health check configuration.

`HealthCheckType` - (Optional) Health check used to validate VM health. Valid values: “INSTANCE_STATE”.

`GracePeriod` - (Optional) The time to allow instances to become healthy.

`AutoHealing` - (Optional) Enable auto-healing of unhealthy VMs.

`Network` - (Required) Defines the Virtual Network and Subnet for your Elastigroup.

`VirtualNetworkName` - (Required) Name of Vnet.

`SubnetName` - (Required) ID of subnet.

`AssignPublicUp` - (Optional, Default: `false`) Assign a public IP to each VM in the Elastigroup.

`Login` - (Required) Describes the login configuration.

`UserName` - (Required) Set admin access for accessing your VMs.

`SshPublicKey` - (Optional) SSH for admin access to Linux VMs. Required for Linux product types.

`Password` - (Optional) Password for admin access to Windows VMs. Required for Windows product types.

`ScheduledTask` - (Optional) Describes the configuration of one or more scheduled tasks.

`IsEnabled` - (Optional, Default: `true`) Describes whether the task is enabled. When true the task should run when false it should not run.

`CronExpression` - (Required) A valid cron expression (`* * * * *`). The cron is running in UTC time zone and is in Unix cron format Cron Expression Validator Script.

`TaskType` - (Required) The task type to run. Valid Values: `backup_ami`, `scale`, `scaleUp`, `roll`, `statefulUpdateCapacity`, `statefulRecycle`.

`ScaleMinCapacity` - (Optional) The min capacity of the group. Should be used when choosing ‘task_type' of ‘scale'.

`ScaleMaxCapacity` - (Optional) The max capacity of the group. Required when ‘task_type' is ‘scale'.

`ScaleTargetCapacity` - (Optional) The target capacity of the group. Should be used when choosing ‘task_type' of ‘scale'.

`Adjustment` - (Optional) The number of instances to add/remove to/from the target capacity when scale is needed.

`AdjustmentPercentage` - (Optional) The percent of instances to add/remove to/from the target capacity when scale is needed.

`BatchSizePercentage` - (Optional) The percentage size of each batch in the scheduled deployment roll. Required when the 'task_type' is 'roll'.


## See Also

* [spotinst_elastigroup_azure](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_azure.html) in the _Terraform Provider Documentation_
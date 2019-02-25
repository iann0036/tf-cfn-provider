# Terraform::Spotinst::ElastigroupAwsBeanstalk

Provides a Spotinst AWS group resource using Elastic Beanstalk.

## Properties

`Name` - (Required) The group name.

`Region` - (Required) The AWS region your group will be created in. Cannot be changed after the group has been created.

`Description` - (Optional) The group description.

`Product` - (Required) Operation system type. Valid values: `"Linux/UNIX"`, `"SUSE Linux"`, `"Windows"`.
For EC2 Classic instances:  `"Linux/UNIX (Amazon VPC)"`, `"SUSE Linux (Amazon VPC)"`, `"Windows (Amazon VPC)"`.

`MaxSize` - (Required) The maximum number of instances the group should have at any time.

`MinSize` - (Required) The minimum number of instances the group should have at any time.

`DesiredCapacity` - (Required) The desired number of instances the group should have at any time.

`BeanstalkEnvironmentName` - (Optional) The name of an existing Beanstalk environment.

`BeanstalkEnvironmentId` - (Optional) The id of an existing Beanstalk environment.

`InstanceTypesSpot` - (Required) One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.

`DeploymentPreferences` - (Optional) Preferences when performing a roll
* `AutomaticRoll` - (Required) Should roll perform automatically
* `BatchSizePercentage` - (Required) Percent size of each batch
* `GracePeriod` - (Required) Amount of time to wait between batches
* `Strategy` - (Optional) Strategy parameters
* `Action` - (Required) Action to take
* `ShouldDrainInstances` - (Required) Bool value if to wait to drain instance.

`AutomaticRoll` - (Required) Should roll perform automatically
* `BatchSizePercentage` - (Required) Percent size of each batch
* `GracePeriod` - (Required) Amount of time to wait between batches
* `Strategy` - (Optional) Strategy parameters
* `Action` - (Required) Action to take
* `ShouldDrainInstances` - (Required) Bool value if to wait to drain instance.

`BatchSizePercentage` - (Required) Percent size of each batch
* `GracePeriod` - (Required) Amount of time to wait between batches
* `Strategy` - (Optional) Strategy parameters
* `Action` - (Required) Action to take
* `ShouldDrainInstances` - (Required) Bool value if to wait to drain instance.

`GracePeriod` - (Required) Amount of time to wait between batches
* `Strategy` - (Optional) Strategy parameters
* `Action` - (Required) Action to take
* `ShouldDrainInstances` - (Required) Bool value if to wait to drain instance.

`Strategy` - (Optional) Strategy parameters
* `Action` - (Required) Action to take
* `ShouldDrainInstances` - (Required) Bool value if to wait to drain instance.

`Action` - (Required) Action to take
* `ShouldDrainInstances` - (Required) Bool value if to wait to drain instance.

`ShouldDrainInstances` - (Required) Bool value if to wait to drain instance.

`ManagedActions` - (Optional) Managed Actions parameters
* `PlatformUpdate` - (Optional) Platform Update parameters
* `PerformAt` - (Required) Actions to perform (options: timeWindow, never)
* `TimeWindow` - (Required) Time Window for when action occurs ex. Mon:23:50-Tue:00:20
* `UpdateLevel` - (Required) - Level to update.

`PlatformUpdate` - (Optional) Platform Update parameters
* `PerformAt` - (Required) Actions to perform (options: timeWindow, never)
* `TimeWindow` - (Required) Time Window for when action occurs ex. Mon:23:50-Tue:00:20
* `UpdateLevel` - (Required) - Level to update.

`PerformAt` - (Required) Actions to perform (options: timeWindow, never)
* `TimeWindow` - (Required) Time Window for when action occurs ex. Mon:23:50-Tue:00:20
* `UpdateLevel` - (Required) - Level to update.

`TimeWindow` - (Required) Time Window for when action occurs ex. Mon:23:50-Tue:00:20
* `UpdateLevel` - (Required) - Level to update.

`UpdateLevel` - (Required) - Level to update.


## See Also

* [spotinst_elastigroup_aws_beanstalk](https://www.terraform.io/docs/providers/spotinst/r/elastigroup_aws_beanstalk.html) in the _Terraform Provider Documentation_
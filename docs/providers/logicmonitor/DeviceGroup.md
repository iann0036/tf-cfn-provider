# Terraform::LogicMonitor::DeviceGroup

Provides a LogicMonitor device group resource. This can be used to create and manage LogicMonitor device groups

## Properties

`Name` - (Required) Name of device group.

`Description` - (Optional) Description of device group.

`ParentId` - (Optional) The id of the parent group for this device group (the root device group has an Id of 1).

`AppliesTo` - (Optional) The Applies to custom query for this group. Setting this field will make this a dynamic group.

`DisableAlerting` - (Optional) Indicates whether alerting is disabled (true) or enabled (false) for this device group.

`Properties` - (Optional) The properties associated with this device group. Any string value pair will work (see example).


## See Also

* [logicmonitor_device_group](https://www.terraform.io/docs/providers/logicmonitor/r/device_group.html) in the _Terraform Provider Documentation_
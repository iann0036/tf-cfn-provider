# Terraform::LogicMonitor::Device

Provides a LogicMonitor device resource. This can be used to create and manage LogicMonitor devices

## Properties

`IpAddr` - (Required) Ip Address/Hostname of device.

`Collector` - (required) The id of the collector that will monitoring the device.

`DisplayName` - (Optional) Display name of device, (default is ip_addr).

`DisableAlerting` - (Optional) The host is created with alerting disabled (default is true).

`HostgroupId` - (Optional) The host group id that specifies which group the device belongs to (multiple host group ids can be added, represented by a comma separated string).

`Properties` - (Optional) The properties associated with this device group. Any string value pair will work (see example).


## See Also

* [logicmonitor_device](https://www.terraform.io/docs/providers/logicmonitor/r/device.html) in the _Terraform Provider Documentation_
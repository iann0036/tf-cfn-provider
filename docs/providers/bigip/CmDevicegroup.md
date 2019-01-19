# Terraform::BIGIP::CmDevicegroup

`BigipCmDevicegroup` A device group is a collection of BIG-IP devices that are configured to securely synchronize their BIG-IP configuration data, and fail over when needed.

## Properties

`BigipCmDevicegroup` - Is the resource  used to configure new device group on the BIG-IP.

`Name` - Is the name of the device Group.

`AutoSync` - Specifies if the device-group will automatically sync configuration data to its members.

`Type` - Specifies if the device-group will be used for failover or resource syncing.

`Device` - Name of the device to be included in device group, this need to be configured before using devicegroup resource.


## See Also

* [bigip_cm_devicegroup](https://www.terraform.io/docs/providers/bigip/r/cm_devicegroup.html) in the _Terraform Provider Documentation_
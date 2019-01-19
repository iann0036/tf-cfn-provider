# Terraform::Packet::Device

Provides a Packet device resource. This can be used to create,
modify, and delete devices.

~> **Note:** All arguments including the root_password and user_data will be stored in
 the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the device.

`Hostname` - The hostname of the device.

`ProjectId` - The ID of the project the device belongs to.

`Facility` - The facility the device is in.

`Plan` - The hardware config of the device.

`Network` - The device's private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 newtworks: private IPv4, public IPv4 and an IPv6 in this order. The fields of the network attribute are:.

`Address` - IPv4 or IPv6 address string.

`Cidr` - bit length of the network mask of the address.

`Gateway` - address of router.

`Public` - whether address is routable from the Internet.

`Family` - IP version - "4" or "6".

`AccessPublicIpv6` - The ipv6 maintenance IP assigned to the device.

`AccessPublicIpv4` - The ipv4 maintenance IP assigned to the device.

`AccessPrivateIpv4` - The ipv4 private IP assigned to the device.

`Locked` - Whether the device is locked.

`BillingCycle` - The billing cycle of the device (monthly or hourly).

`OperatingSystem` - The operating system running on the device.

`State` - The status of the device.

`Created` - The timestamp for when the device was created.

`Updated` - The timestamp for the last time the device was updated.

`Tags` - Tags attached to the device.

`Description` - Description string for the device.

`HardwareReservationId` - The id of hardware reservation which this device occupies.

`RootPassword` - Root password to the server (disabled after 24 hours).

## See Also

* [packet_device](https://www.terraform.io/docs/providers/packet/r/device.html) in the _Terraform Provider Documentation_
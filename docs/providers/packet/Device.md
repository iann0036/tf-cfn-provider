# Terraform::Packet::Device

Provides a Packet device resource. This can be used to create,
modify, and delete devices.

~> **Note:** All arguments including the root_password and user_data will be stored in
 the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Hostname` - (Required) The device name.

`ProjectId` - (Required) The id of the project in which to create the device.

`OperatingSystem` - (Required) The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.net/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.

`Facility` - (Deprecated) The facility in which to create the device.

`Facilities` - List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://www.packet.net/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.

`Plan` - (Required) The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.net/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.

`BillingCycle` - (Required) monthly or hourly.

`Tags` - Tags attached to the device.

`Description` - Description string for the device.

`ProjectSshKeyIds` - Array of IDs of the project SSH keys which should be added to the device. If you omit this, SSH keys of all the members of the parent project will be added to the device. If you specify this array, only the listed project SSH keys will be added. Project SSH keys can be created with the [packet_project_ssh_key][packet_project_ssh_key.html] resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the device.

`Hostname` - The hostname of the device.

`ProjectId` - The ID of the project the device belongs to.

`Facility` - The facility where the device is deployed.

`Plan` - The hardware config of the device.

`Network` - The device's private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:.

`Address` - IPv4 or IPv6 address string.

`Cidr` - bit length of the network mask of the address.

`Gateway` - address of router.

`Public` - whether the address is routable from the Internet.

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

`SshKeyIds` - List of IDs of SSH keys deployed in the device, can be both user and project SSH keys.

## See Also

* [packet_device](https://www.terraform.io/docs/providers/packet/r/device.html) in the _Terraform Provider Documentation_
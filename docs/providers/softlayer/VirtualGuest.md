# Terraform::SoftLayer::VirtualGuest

Provides virtual guest resource. This allows virtual guests to be created, updated
and deleted. For additional details please refer to [API documentation](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest).

## Properties

`Name` - (Required, string) Hostname for the computing instance.

`Domain` - (Required, string) Domain for the computing instance.

`Cpu` - (Required, int) The number of CPU cores to allocate.

`Ram` - (Required, int) The amount of memory to allocate in megabytes.

`Region` - (Required, string) Specifies which datacenter the instance is to be provisioned in.

`HourlyBilling` - (Required, boolean) Specifies the billing type for the instance. When `true`, the computing instance will be billed on hourly usage, otherwise it will be billed on a monthly basis.

`LocalDisk` - (Required, boolean) Specifies the disk type for the instance. When `true`, the disks for the computing instance will be provisioned on the host which it runs, otherwise SAN disks will be provisioned.

`DedicatedAcctHostOnly` - (Optional, boolean) Specifies whether or not the instance must only run on hosts with instances from the same account.

`Image` - (Conditionally required, string) An identifier for the operating system to provision the computing instance with. Disallowed when `blockDeviceTemplateGroup.globalIdentifier` is provided, as the template will specify the operating system.

`BlockDeviceTemplateGroupGid` - (Conditionally required, string) A global identifier for the template to be used to provision the computing instance. Disallowed when `operatingSystemReferenceCode` is provided, as the template will specify the operating system.

`PublicNetworkSpeed` - (Optional, int, default 10) Specifies the connection speed for the instance's network components.

`PrivateNetworkOnly` - (Optional, boolean, default false) Specifies whether or not the instance only has access to the private network. When true this flag specifies that a compute instance is to only have access to the private network.

`FrontendVlanId` - (Optional, int) Specifies the network VLAN which is to be used for the front end interface of the computing instance.

`BackendVlanId` - (Optional, int) Specifies the network VLAN which is to be used for the back end interface of the computing instance.

`Disks` - (Optional, array) Block device and disk image settings for the computing instance.

`UserData` - (Optional, string) Arbitrary data to be made available to the computing instance.

`SshKeys` - (Optional, array) SSH keys to install on the computing instance upon provisioning.

`Ipv4Address` - (Optional, string) Uses `editObject` call, template data [defined here](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest).

`Ipv4AddressPrivate` - (Optional, string) Uses `editObject` call, template data [defined here](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest).

`PostInstallScriptUri` - (Optional, string) As defined in the [SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions).


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual guest.

## See Also

* [softlayer_virtual_guest](https://www.terraform.io/docs/providers/softlayer/r/virtual_guest.html) in the _Terraform Provider Documentation_
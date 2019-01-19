# Terraform::SelVPC::ResellFloatingipV2

Manages a V2 floatingip resource within Resell Selectel VPC.

## Properties

`ProjectId` - (Required) An associated Selectel VPC project. Changing this creates a new floating IP.

`Region` - (Required) A region of where the floating IP resides. Changing this creates a new floating IP.


## Return Values

### Fn::GetAtt

`PortId` - Contains id of the Networking service port.

`FloatingIpAddress` - Contains floating IP address.

`FixedIpAddress` - Contains internal IP address of the Networking service port.

`Status` - Shows if the license is used or not.

`Servers` - Shows information about servers that use this floating IP. Contains.

## See Also

* [selvpc_resell_floatingip_v2](https://www.terraform.io/docs/providers/selvpc/r/resell_floatingip_v2.html) in the _Terraform Provider Documentation_
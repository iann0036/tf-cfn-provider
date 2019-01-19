# Terraform::CloudStack::Nic

Creates an additional NIC to add a VM to the specified network.

## Properties

`NetworkId` - (Required) The ID of the network to plug the NIC into. Changing this forces a new resource to be created.

`IpAddress` - (Optional) The IP address to assign to the NIC. Changing this forces a new resource to be created.

`VirtualMachineId` - (Required) The ID of the virtual machine to which to attach the NIC. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the NIC.

`IpAddress` - The assigned IP address.

## See Also

* [cloudstack_nic](https://www.terraform.io/docs/providers/cloudstack/r/nic.html) in the _Terraform Provider Documentation_
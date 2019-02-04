# Terraform::CloudStack::SecondaryIpaddress

Assigns a secondary IP to a NIC.

## Properties

`IpAddress` - (Optional) The IP address to bind the to NIC. If not supplied
an IP address will be selected randomly. Changing this forces a new resource
to be	created.

`NicId` - (Optional) The NIC ID to which you want to attach the secondary IP
address. Changing this forces a new resource to be created (defaults to the
ID of the primary NIC).

`VirtualMachineId` - (Required) The ID of the virtual machine to which you
want to attach the secondary IP address. Changing this forces a new resource
to be created.


## Return Values

### Fn::GetAtt

`Id` - The secondary IP address ID.

`IpAddress` - The IP address that was acquired and associated.

## See Also

* [cloudstack_secondary_ipaddress](https://www.terraform.io/docs/providers/cloudstack/r/secondary_ipaddress.html) in the _Terraform Provider Documentation_
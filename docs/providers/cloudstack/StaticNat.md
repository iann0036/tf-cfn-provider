# Terraform::CloudStack::StaticNat

Enables static NAT for a given IP address

## Properties

`IpAddressId` - (Required) The public IP address ID for which static NAT will be enabled. Changing this forces a new resource to be created.

`VirtualMachineId` - (Required) The virtual machine ID to enable the static NAT feature for. Changing this forces a new resource to be created.

`VmGuestIp` - (Optional) The virtual machine IP address to forward the static NAT traffic to (useful when the virtual machine has secondary NICs or IP addresses). Changing this forces a new resource to be created.

`Project` - (Optional) The name or ID of the project to deploy this instance to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The static nat ID.

`VmGuestIp` - The IP address of the virtual machine that is used.

## See Also

* [cloudstack_static_nat](https://www.terraform.io/docs/providers/cloudstack/r/static_nat.html) in the _Terraform Provider Documentation_
# Terraform::CloudStack::PortForward

Creates port forwards.

## Properties

`IpAddressId` - (Required) The IP address ID for which to create the port forwards. Changing this forces a new resource to be created.

`Managed` - (Optional) USE WITH CAUTION! If enabled all the port forwards for this IP address will be managed by this resource. This means it will delete all port forwards that are not in your config! (defaults false).

`Project` - (Optional) The name or ID of the project to create this port forward in. Changing this forces a new resource to be created.

`Forward` - (Required) Can be specified multiple times. Each forward block supports fields documented below.

### Forward Properties

`Protocol` - (Required) The name of the protocol to allow. Valid options are: `tcp` and `udp`.

`PrivatePort` - (Required) The private port to forward to.

`PublicPort` - (Required) The public port to forward from.

`VirtualMachineId` - (Required) The ID of the virtual machine to forward to.

`VmGuestIp` - (Optional) The virtual machine IP address for the port forwarding rule (useful when the virtual machine has secondairy NICs or IP addresses).


## Return Values

### Fn::GetAtt

`Id` - The ID of the IP address for which the port forwards are created.

`VmGuestIp` - The IP address of the virtual machine that is used.

## See Also

* [cloudstack_port_forward](https://www.terraform.io/docs/providers/cloudstack/r/port_forward.html) in the _Terraform Provider Documentation_
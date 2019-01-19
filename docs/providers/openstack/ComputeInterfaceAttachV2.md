# Terraform::OpenStack::ComputeInterfaceAttachV2

Attaches a Network Interface (a Port) to an Instance using the OpenStack
Compute (Nova) v2 API.

## Properties

`Region` - (Optional) The region in which to create the interface attachment. If omitted, the `Region` argument of the provider is used. Changing this creates a new attachment.

`InstanceId` - (Required) The ID of the Instance to attach the Port or Network to.

`PortId` - (Optional) The ID of the Port to attach to an Instance. _NOTE_: This option and `NetworkId` are mutually exclusive.

`NetworkId` - (Optional) The ID of the Network to attach to an Instance. A port will be created automatically. _NOTE_: This option and `PortId` are mutually exclusive.

`FixedIp` - (Optional) An IP address to assosciate with the port. _NOTE_: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`InstanceId` - See Properties above.

`PortId` - See Properties above.

`NetworkId` - See Properties above.

`FixedIp` - See Properties above.

## See Also

* [openstack_compute_interface_attach_v2](https://www.terraform.io/docs/providers/openstack/r/compute_interface_attach_v2.html) in the _Terraform Provider Documentation_
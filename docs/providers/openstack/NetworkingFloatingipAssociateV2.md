# Terraform::OpenStack::NetworkingFloatingipAssociateV2

Associates a floating IP to a port. This is useful for situations
where you have a pre-allocated floating IP or are unable to use the
`Terraform::OpenStack::NetworkingFloatingipV2` resource to create a floating IP.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).

`FloatingIp` - (Required) IP Address of an existing floating IP.

`PortId` - (Required) ID of an existing port with at least one IP address to
associate with this floating IP.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`FloatingIp` - See Properties above.

`PortId` - See Properties above.

## See Also

* [openstack_networking_floatingip_associate_v2](https://www.terraform.io/docs/providers/openstack/r/networking_floatingip_associate_v2.html) in the _Terraform Provider Documentation_
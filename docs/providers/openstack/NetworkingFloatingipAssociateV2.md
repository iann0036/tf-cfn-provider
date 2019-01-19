# Terraform::OpenStack::NetworkingFloatingipAssociateV2

Associates a floating IP to a port. This is useful for situations
where you have a pre-allocated floating IP or are unable to use the
`openstack_networking_floatingip_v2` resource to create a floating IP.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`FloatingIp` - See Argument Reference above.

`PortId` - See Argument Reference above.

## See Also

* [openstack_networking_floatingip_associate_v2](https://www.terraform.io/docs/providers/openstack/r/networking_floatingip_associate_v2.html) in the _Terraform Provider Documentation_
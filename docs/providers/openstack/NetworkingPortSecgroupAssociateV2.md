# Terraform::OpenStack::NetworkingPortSecgroupAssociateV2

Manages a V2 port's security groups within OpenStack. Useful, when the port was
created not by Terraform (e.g. Manila or LBaaS). It should not be used, when the
port was created directly within Terraform.

When the resource is deleted, Terraform doesn't delete the port, but unsets the
list of user defined security group IDs.  However, if `Enforce` is set to `true`
and the resource is deleted, Terraform will remove all assigned security group
IDs.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client.
A networking client is needed to manage a port. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
resource.

`PortId` - (Required) An UUID of the port to apply security groups to.

`SecurityGroupIds` - (Required) A list of security group IDs to apply to
the port. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).

`Enforce` - (Optional) Whether to replace or append the list of security
groups, specified in the `SecurityGroupIds`. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`PortId` - See Properties above.

`SecurityGroupIds` - See Properties above.

`AllSecurityGroupIds` - The collection of Security Group IDs on the port.

## See Also

* [openstack_networking_port_secgroup_associate_v2](https://www.terraform.io/docs/providers/openstack/r/networking_port_secgroup_associate_v2.html) in the _Terraform Provider Documentation_
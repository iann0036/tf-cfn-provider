# Terraform::OpenStack::NetworkingAddressscopeV2

Manages a V2 Neutron addressscope resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the `Region` argument of the provider is used. Changing this creates a new
address-scope.

`Name` - (Required) The name of the address-scope. Changing this updates the
name of the existing address-scope.

`IpVersion` - (Optional) IP version, either 4 (default) or 6. Changing this
creates a new address-scope.

`Shared` - (Optional) Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.

`ProjectId` - (Optional) The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`IpVersion` - See Properties above.

`Shared` - See Properties above.

`ProjectId` - See Properties above.

## See Also

* [openstack_networking_addressscope_v2](https://www.terraform.io/docs/providers/openstack/r/networking_addressscope_v2.html) in the _Terraform Provider Documentation_
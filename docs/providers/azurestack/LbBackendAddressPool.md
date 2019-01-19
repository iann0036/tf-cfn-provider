# Terraform::AzureStack::LbBackendAddressPool

Manages a LoadBalancer Backend Address Pool.

~> **NOTE:** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the LoadBalancer to which the resource is attached.

## See Also

* [azurestack_lb_backend_address_pool](https://www.terraform.io/docs/providers/azurestack/r/lb_backend_address_pool.html) in the _Terraform Provider Documentation_
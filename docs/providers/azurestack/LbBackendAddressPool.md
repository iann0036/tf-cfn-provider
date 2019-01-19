# Terraform::AzureStack::LbBackendAddressPool

Manages a LoadBalancer Backend Address Pool.

~> **NOTE:** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

## Properties

`Name` - (Required) Specifies the name of the Backend Address Pool.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource.

`LoadbalancerId` - (Required) The ID of the LoadBalancer in which to create the Backend Address Pool.


## Return Values

### Fn::GetAtt

`Id` - The ID of the LoadBalancer to which the resource is attached.

## See Also

* [azurestack_lb_backend_address_pool](https://www.terraform.io/docs/providers/azurestack/r/lb_backend_address_pool.html) in the _Terraform Provider Documentation_
# Terraform::AzureRM::LbBackendAddressPool

Manage a Load Balancer Backend Address Pool.

~> **NOTE:** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Properties

`Name` - (Required) Specifies the name of the Backend Address Pool.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource.

`LoadbalancerId` - (Required) The ID of the Load Balancer in which to create the Backend Address Pool.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Backend Address Pool.

`BackendIpConfigurations` - The Backend IP Configurations associated with this Backend Address Pool.

`LoadBalancingRules` - The Load Balancing Rules associated with this Backend Address Pool.

## See Also

* [azurerm_lb_backend_address_pool](https://www.terraform.io/docs/providers/azurerm/r/lb_backend_address_pool.html) in the _Terraform Provider Documentation_
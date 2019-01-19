# Terraform::AzureRM::LbBackendAddressPool

Manage a Load Balancer Backend Address Pool.

~> **NOTE:** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the Backend Address Pool.

`BackendIpConfigurations` - The Backend IP Configurations associated with this Backend Address Pool.

`LoadBalancingRules` - The Load Balancing Rules associated with this Backend Address Pool.

## See Also

* [azurerm_lb_backend_address_pool](https://www.terraform.io/docs/providers/azurerm/r/lb_backend_address_pool.html) in the _Terraform Provider Documentation_
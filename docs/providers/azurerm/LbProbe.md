# Terraform::AzureRM::LbProbe

Manages a LoadBalancer Probe Resource.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the Load Balancer to which the resource is attached.

## See Also

* [azurerm_lb_probe](https://www.terraform.io/docs/providers/azurerm/r/lb_probe.html) in the _Terraform Provider Documentation_
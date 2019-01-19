# Terraform::AzureRM::LbNatRule

Manages a Load Balancer NAT Rule.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Properties

`Name` - (Required) Specifies the name of the NAT Rule.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource.

`LoadbalancerId` - (Required) The ID of the Load Balancer in which to create the NAT Rule.

`FrontendIpConfigurationName` - (Required) The name of the frontend IP configuration exposing this rule.

`Protocol` - (Required) The transport protocol for the external endpoint. Possible values are `Udp`, `Tcp` or `All`.

`FrontendPort` - (Required) The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

`BackendPort` - (Required) The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

`EnableFloatingIp` - (Optional) Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Load Balancer to which the resource is attached.

## See Also

* [azurerm_lb_nat_rule](https://www.terraform.io/docs/providers/azurerm/r/lb_nat_rule.html) in the _Terraform Provider Documentation_
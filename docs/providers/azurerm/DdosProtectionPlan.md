# Terraform::AzureRM::DdosProtectionPlan

Manages an Azure DDoS Protection Plan.

-> **NOTE** Azure only allow `one` DDoS Protection Plan per region.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Resource ID of the DDoS Protection Plan.

`VirtualNetworkIds` - The Resource ID list of the Virtual Networks associated with DDoS Protection Plan.

## See Also

* [azurerm_ddos_protection_plan](https://www.terraform.io/docs/providers/azurerm/r/ddos_protection_plan.html) in the _Terraform Provider Documentation_
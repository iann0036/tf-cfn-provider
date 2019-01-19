# Terraform::AzureRM::DdosProtectionPlan

Manages an Azure DDoS Protection Plan.

-> **NOTE** Azure only allow `one` DDoS Protection Plan per region.

## Properties

`Name` - (Required) Specifies the name of the DDoS Protection Plan. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the resource. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Resource ID of the DDoS Protection Plan.

`VirtualNetworkIds` - The Resource ID list of the Virtual Networks associated with DDoS Protection Plan.

## See Also

* [azurerm_ddos_protection_plan](https://www.terraform.io/docs/providers/azurerm/r/ddos_protection_plan.html) in the _Terraform Provider Documentation_
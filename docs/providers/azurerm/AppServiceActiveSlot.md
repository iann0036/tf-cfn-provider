# Terraform::AzureRM::AppServiceActiveSlot

Promotes an App Service Slot to Production within an App Service.

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `Terraform::AzureRM::AppService` resource will be overwritten when promoting a Slot using the `azurermAppServiceActiveSlot` resource.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.

`AppServiceName` - (Required) The name of the App Service within which the Slot exists.  Changing this forces a new resource to be created.

`AppServiceSlotName` - (Required) The name of the App Service Slot which should be promoted to the Production Slot within the App Service.


## See Also

* [azurerm_app_service_active_slot](https://www.terraform.io/docs/providers/azurerm/r/app_service_active_slot.html) in the _Terraform Provider Documentation_
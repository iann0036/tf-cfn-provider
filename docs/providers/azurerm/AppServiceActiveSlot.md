# Terraform::AzureRM::AppServiceActiveSlot

Promotes an App Service Slot to Production within an App Service.

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [azurerm_app_service_active_slot](https://www.terraform.io/docs/providers/azurerm/r/app_service_active_slot.html) in the _Terraform Provider Documentation_
# Terraform::AzureRM::AppServiceSlot

Manages an App Service Slot (within an App Service).

-> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azurerm_app_service` resource will be overwritten when promoting a Slot using the `azurerm_app_service_active_slot` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the App Service Slot.

`DefaultSiteHostname` - The Default Hostname associated with the App Service Slot - such as `mysite.azurewebsites.net`.

## See Also

* [azurerm_app_service_slot](https://www.terraform.io/docs/providers/azurerm/r/app_service_slot.html) in the _Terraform Provider Documentation_
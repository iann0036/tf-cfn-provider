# Terraform::AzureRM::AppServiceCustomHostnameBinding

Manages a Hostname Binding within an App Service.

## Properties

`Hostname` - (Required) Specifies the Custom Hostname to use for the App Service, example `www.example.com`. Changing this forces a new resource to be created.

`AppServiceName` - (Required) The name of the App Service in which to add the Custom Hostname Binding. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the App Service exists. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the App Service Custom Hostname Binding.

## See Also

* [azurerm_app_service_custom_hostname_binding](https://www.terraform.io/docs/providers/azurerm/r/app_service_custom_hostname_binding.html) in the _Terraform Provider Documentation_
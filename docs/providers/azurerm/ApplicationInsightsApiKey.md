# Terraform::AzureRM::ApplicationInsightsApiKey

Manages an Application Insights API key.

## Properties

`Name` - (Required) Specifies the name of the Application Insights API key. Changing this forces a
new resource to be created.

`ApplicationInsightsId` - (Required) The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.

`ReadPermissions` - (Optional) Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created.

`WritePermissions` - (Optional) Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Application Insights API key.

`ApiKey` - The API Key secret (Sensitive).

## See Also

* [azurerm_application_insights_api_key](https://www.terraform.io/docs/providers/azurerm/r/application_insights_api_key.html) in the _Terraform Provider Documentation_
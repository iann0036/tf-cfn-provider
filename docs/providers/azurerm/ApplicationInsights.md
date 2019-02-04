# Terraform::AzureRM::ApplicationInsights

Manage an Application Insights component.

## Properties

`Name` - (Required) Specifies the name of the Application Insights component. Changing this forces a
new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the Application Insights component.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ApplicationType` - (Required) Specifies the type of Application Insights to create. Valid values are `Java`, `iOS`, `MobileCenter`, `Other`, `Phone`, `Store`, `Web` and `Node.JS`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Application Insights component.

`AppId` - The App ID associated with this Application Insights component.

`InstrumentationKey` - The Instrumentation Key for this Application Insights component.

## See Also

* [azurerm_application_insights](https://www.terraform.io/docs/providers/azurerm/r/application_insights.html) in the _Terraform Provider Documentation_
# Terraform::AzureRM::LogicAppActionCustom

Manages a Custom Action within a Logic App Workflow

## Properties

`Name` - (Required) Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

`LogicAppId` - (Required) Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

`Body` - (Required) Specifies the JSON Blob defining the Body of this Custom Action.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Action within the Logic App Workflow.

## See Also

* [azurerm_logic_app_action_custom](https://www.terraform.io/docs/providers/azurerm/r/logic_app_action_custom.html) in the _Terraform Provider Documentation_
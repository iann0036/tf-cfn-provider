# Terraform::AzureRM::LogicAppActionHttp

Manages an HTTP Action within a Logic App Workflow

## Properties

`Name` - (Required) Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

`LogicAppId` - (Required) Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

`Method` - (Required) Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.

`Uri` - (Required) Specifies the URI which will be called when this HTTP Action is triggered.

`Body` - (Optional) Specifies the HTTP Body that should be sent to the `Uri` when this HTTP Action is triggered.

`Headers` - (Optional) Specifies a Map of Key-Value Pairs that should be sent to the `Uri` when this HTTP Action is triggered.


## Return Values

### Fn::GetAtt

`Id` - The ID of the HTTP Action within the Logic App Workflow.

## See Also

* [azurerm_logic_app_action_http](https://www.terraform.io/docs/providers/azurerm/r/logic_app_action_http.html) in the _Terraform Provider Documentation_
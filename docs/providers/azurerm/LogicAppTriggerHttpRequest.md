# Terraform::AzureRM::LogicAppTriggerHttpRequest

Manages a HTTP Request Trigger within a Logic App Workflow

## Properties

`Name` - (Required) Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

`LogicAppId` - (Required) Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

`Schema` - (Required) A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.

`Method` - (Optional) Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.

`RelativePath` - (Optional) Specifies the Relative Path used for this Request.


## Return Values

### Fn::GetAtt

`Id` - The ID of the HTTP Request Trigger within the Logic App Workflow.

## See Also

* [azurerm_logic_app_trigger_http_request](https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_http_request.html) in the _Terraform Provider Documentation_
# Terraform::AzureRM::LogicAppTriggerRecurrence

Manages a Recurrence Trigger within a Logic App Workflow

## Properties

`Name` - (Required) Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.

`LogicAppId` - (Required) Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

`Frequency` - (Required) Specifies the Frequency at which this Trigger should be run. Possible values include `Month`, `Week`, `Day`, `Hour`, `Minute` and `Second`.

`Interval` - (Required) Specifies interval used for the Frequency, for example a value of `4` for `Interval` and `hour` for `Frequency` would run the Trigger every 4 hours.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Recurrence Trigger within the Logic App Workflow.

## See Also

* [azurerm_logic_app_trigger_recurrence](https://www.terraform.io/docs/providers/azurerm/r/logic_app_trigger_recurrence.html) in the _Terraform Provider Documentation_
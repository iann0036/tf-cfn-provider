# Terraform::AzureRM::AutomationSchedule

Manages a Automation Schedule.

## Properties

`Name` - (Required) Specifies the name of the Schedule. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

`AutomationAccountName` - (Required) The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

`Frequency` - (Required) The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

`Description` -  (Optional) A description for this Schedule.

`Interval` -  (Optional) The number of `Frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.

`StartTime` -  (Optional) Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.

`ExpiryTime` -  (Optional) The end time of the schedule.

`Timezone` - (Optional) The timezone of the start time. Defaults to `UTC`. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx.

`WeekDays` - (Optional) List of days of the week that the job should execute on. Only valid when frequency is `Week`.

`MonthDays` - (Optional) List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.

`MonthlyOccurrence` - (Optional) List of occurrences of days within a month. Only valid when frequency is `Month`. The `MonthlyOccurrence` block supports fields documented below.

`Day` - (Required) Day of the occurrence. Must be one of `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`.

`Occurrence` - (Required) Occurrence of the week within the month. Must be between `1` and `5`. `-1` for last week within the month.


## Return Values

### Fn::GetAtt

`Id` - The Automation Schedule ID.

## See Also

* [azurerm_automation_schedule](https://www.terraform.io/docs/providers/azurerm/r/automation_schedule.html) in the _Terraform Provider Documentation_
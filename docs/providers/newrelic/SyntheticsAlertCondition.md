# Terraform::NewRelic::SyntheticsAlertCondition



## Properties

`PolicyId` - (Required) The ID of the policy where this condition should be used. * `Name` - (Required) The title of this condition. * `MonitorId` - (Required) The ID of the Synthetics monitor to be referenced in the alert condition. * `RunbookUrl` - (Optional) Runbook URL to display in notifications. * `Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

`Name` - (Required) The title of this condition. * `MonitorId` - (Required) The ID of the Synthetics monitor to be referenced in the alert condition. * `RunbookUrl` - (Optional) Runbook URL to display in notifications. * `Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

`MonitorId` - (Required) The ID of the Synthetics monitor to be referenced in the alert condition. * `RunbookUrl` - (Optional) Runbook URL to display in notifications. * `Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

`RunbookUrl` - (Optional) Runbook URL to display in notifications. * `Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

`Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Synthetics alert condition.

## See Also

* [newrelic_synthetics_alert_condition](https://www.terraform.io/docs/providers/newrelic/r/synthetics_alert_condition.html) in the _Terraform Provider Documentation_
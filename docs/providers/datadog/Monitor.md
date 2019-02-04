# Terraform::Datadog::Monitor

Provides a Datadog monitor resource. This can be used to create and manage Datadog monitors.

## Properties

`Type` - (Required) The type of the monitor, chosen from:.

`Name` - (Required) Name of Datadog monitor.

`Query` - (Required) The monitor query to notify on. Note this is not the same query you see in the UI and
the syntax is different depending on the monitor `Type`, please see the [API Reference](https://docs.datadoghq.com/api/?lang=python#create-a-monitor) for details. **Warning:** `terraform plan` won't perform any validation of the query contents.

`Message` - (Required) A message to include with notifications for this monitor.
Email notifications can be sent to specific users by using the same '@username' notation as events.

`EscalationMessage` - (Optional) A message to include with a re-notification. Supports the '@username'
notification allowed elsewhere.

`Thresholds` - (Optional).


## Return Values

### Fn::GetAtt

`Id` - ID of the Datadog monitor.

## See Also

* [datadog_monitor](https://www.terraform.io/docs/providers/datadog/r/monitor.html) in the _Terraform Provider Documentation_
# Terraform::Datadog::Monitor

Provides a Datadog monitor resource. This can be used to create and manage Datadog monitors.

## Properties

`Type` - (Required) The type of the monitor, chosen from: * `Metric alert` * `Service check` * `Event alert` * `Query alert` * `Composite` * `Log alert`.

`Name` - (Required) Name of Datadog monitor.

`Query` - (Required) The monitor query to notify on. Note this is not the same query you see in the UI and the syntax is different depending on the monitor `Type`, please see the [API Reference](https://docs.datadoghq.com/api/?lang=python#create-a-monitor) for details. **Warning:** `terraform plan` won't perform any validation of the query contents.

`Message` - (Required) A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the same '@username' notation as events.

`EscalationMessage` - (Optional) A message to include with a re-notification. Supports the '@username' notification allowed elsewhere.

`Thresholds` - (Optional) * Metric alerts: A dictionary of thresholds by threshold type. Currently we have four threshold types for metric alerts: critical, critical recovery, warning, and warning recovery. Critical is defined in the query, but can also be specified in this option. Warning and recovery thresholds can only be specified using the thresholds option. Example usage: ``` thresholds { critical          = 90 critical_recovery = 85 warning           = 80 warning_recovery  = 75 } ``` **Warning:** the `critical` threshold value must match the one contained in the `Query` argument. The `threshold` from the previous example is valid along with a query like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} > 90` but along with something like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} > 95` would make the Datadog API return a HTTP error 400, complaining "The value provided for parameter 'query' is invalid". * Service checks: A dictionary of thresholds by status. Because service checks can have multiple thresholds, we don't define them directly in the query. Default values: ``` thresholds { ok       = 1 critical = 1 warning  = 1 unknown  = 1 } ```.


## Return Values

### Fn::GetAtt

`Id` - ID of the Datadog monitor.

## See Also

* [datadog_monitor](https://www.terraform.io/docs/providers/datadog/r/monitor.html) in the _Terraform Provider Documentation_
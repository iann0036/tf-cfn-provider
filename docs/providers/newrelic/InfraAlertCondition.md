# Terraform::NewRelic::InfraAlertCondition



## Properties

`PolicyId` - (Required) The ID of the alert policy where this condition should be used.
* `Name` - (Required) The Infrastructure alert condition's name.
* `Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.
* `Type` - (Required) The type of Infrastructure alert condition: "infra_process_running", "infra_metric", or "infra_host_not_reporting".
* `Event` - (Required) The metric event; for example, system metrics, process metrics, storage metrics, or network metrics.
* `Select` - (Required) The attribute name to identify the type of metric condition; for example, "network", "process", "system", or "storage".
* `Comparison` - (Required) The operator used to evaluate the threshold value; "above", "below", "equal".
* `Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Name` - (Required) The Infrastructure alert condition's name.
* `Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.
* `Type` - (Required) The type of Infrastructure alert condition: "infra_process_running", "infra_metric", or "infra_host_not_reporting".
* `Event` - (Required) The metric event; for example, system metrics, process metrics, storage metrics, or network metrics.
* `Select` - (Required) The attribute name to identify the type of metric condition; for example, "network", "process", "system", or "storage".
* `Comparison` - (Required) The operator used to evaluate the threshold value; "above", "below", "equal".
* `Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.
* `Type` - (Required) The type of Infrastructure alert condition: "infra_process_running", "infra_metric", or "infra_host_not_reporting".
* `Event` - (Required) The metric event; for example, system metrics, process metrics, storage metrics, or network metrics.
* `Select` - (Required) The attribute name to identify the type of metric condition; for example, "network", "process", "system", or "storage".
* `Comparison` - (Required) The operator used to evaluate the threshold value; "above", "below", "equal".
* `Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Type` - (Required) The type of Infrastructure alert condition: "infra_process_running", "infra_metric", or "infra_host_not_reporting".
* `Event` - (Required) The metric event; for example, system metrics, process metrics, storage metrics, or network metrics.
* `Select` - (Required) The attribute name to identify the type of metric condition; for example, "network", "process", "system", or "storage".
* `Comparison` - (Required) The operator used to evaluate the threshold value; "above", "below", "equal".
* `Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Event` - (Required) The metric event; for example, system metrics, process metrics, storage metrics, or network metrics.
* `Select` - (Required) The attribute name to identify the type of metric condition; for example, "network", "process", "system", or "storage".
* `Comparison` - (Required) The operator used to evaluate the threshold value; "above", "below", "equal".
* `Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Select` - (Required) The attribute name to identify the type of metric condition; for example, "network", "process", "system", or "storage".
* `Comparison` - (Required) The operator used to evaluate the threshold value; "above", "below", "equal".
* `Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Comparison` - (Required) The operator used to evaluate the threshold value; "above", "below", "equal".
* `Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Critical` - (Required) Identifies the critical threshold parameters for triggering an alert notification. See [Thresholds](#thresholds) below for details.
* `Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Warning` - (Optional) Identifies the warning threshold parameters. See [Thresholds](#thresholds) below for details.
* `Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`Where` - (Optional) Infrastructure host filter for the alert condition.
* `ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`ProcessWhere` - (Optional) Any filters applied to processes; for example: `"commandName = 'java'"`.
* `IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.

`IntegrationProvider` - (Optional) For alerts on integrations, use this instead of `Event`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Infrastructure alert condition.

## See Also

* [newrelic_infra_alert_condition](https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition.html) in the _Terraform Provider Documentation_
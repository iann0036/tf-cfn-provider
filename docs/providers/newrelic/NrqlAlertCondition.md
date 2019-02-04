# Terraform::NewRelic::NrqlAlertCondition



## Properties

`PolicyId` - (Required) The ID of the policy where this condition should be used.

`Name` - (Required) The title of the condition.

`RunbookUrl` - (Optional) Runbook URL to display in notifications.

`Enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

`Term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

`Nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.

`ValueFunction` - (Optional) Possible values are `single_value`, `sum`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the NRQL alert condition.

## See Also

* [newrelic_nrql_alert_condition](https://www.terraform.io/docs/providers/newrelic/r/nrql_alert_condition.html) in the _Terraform Provider Documentation_
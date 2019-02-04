# Terraform::NewRelic::AlertCondition



## Properties

`PolicyId` - (Required) The ID of the policy where this condition should be used.

`Name` - (Required) The title of the condition.

`Type` - (Required) The type of condition. One of: `apm_app_metric`, `apm_jvm_metric`, `apm_kt_metric`, `servers_metric`, `browser_metric`, `mobile_metric`.

`Entities` - (Required) The instance IDS associated with this condition.

`Metric` - (Required) The metric field accepts parameters based on the `Type` set.

`GcMetric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`. This is required if you are using `apm_jvm_metric` with `gc_cpu_time` condition type.

`ViolationCloseTimer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.

`RunbookUrl` - (Optional) Runbook URL to display in notifications.

`ConditionScope` - (Optional) `instance` or `application`.  This is required if you are using the JVM plugin in New Relic.

`Term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

`UserDefinedMetric` - (Optional) A custom metric to be evaluated.

`UserDefinedValueFunction` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the alert condition.

## See Also

* [newrelic_alert_condition](https://www.terraform.io/docs/providers/newrelic/r/alert_condition.html) in the _Terraform Provider Documentation_
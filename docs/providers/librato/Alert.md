# Terraform::Librato::Alert

Provides a Librato Alert resource. This can be used to
create and manage alerts on Librato.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the alert.

`Name` - The name of the alert.

`Description` - (Required) Description of the alert.

`Active` - whether the alert is active (can be triggered). Defaults to true.

`RearmSeconds` - minimum amount of time between sending alert notifications, in seconds.

`Services` - list of notification service IDs.

`Condition` - A trigger condition for the alert. Conditions documented below.

`Type` - The type of condition. Must be one of `above`, `below` or `absent`.

`MetricName` - The name of the metric this alert condition applies to.

`Source` - A source expression which identifies which sources for the given metric to monitor.

`DetectReset` - boolean: toggles the method used to calculate the delta from the previous sample when the summary_function is `derivative`.

`Duration` - number of seconds condition must be true to fire the alert (required for type `absent`).

`Threshold` - float: measurements over this number will fire the alert (only for `above` or `below`).

`SummaryFunction` - Indicates which statistic of an aggregated measurement to alert on. ((only for `above` or `below`).

`RunbookUrl` - a URL for the runbook to be followed when this alert is firing. Used in the Librato UI if set.

## See Also

* [librato_alert](https://www.terraform.io/docs/providers/librato/r/alert.html) in the _Terraform Provider Documentation_
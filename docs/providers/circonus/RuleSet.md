# Terraform::Circonus::RuleSet

The ``Terraform::Circonus::RuleSet`` resource creates and manages a
[Circonus Rule Set](https://login.circonus.com/resources/api/calls/rule_set).

## Properties

`Check` - (Required) The Circonus ID that this Rule Set will use to search for a metric stream to alert on.

`If` - (Required) One or more ordered predicate clauses that describe when Circonus should generate a notification.  See below for details on the structure of an `If` configuration clause.

`Link` - (Optional) A link to external documentation (or anything else you feel is important) when a notification is sent.  This value will show up in email alerts and the Circonus UI.

`MetricType` - (Optional) The type of metric this rule set will operate on. Valid values are `numeric` (the default) and `text`.

`Notes` - (Optional) Notes about this rule set.

`Parent` - (Optional) A Circonus Metric ID that, if specified and active with a severity 1 alert, will silence this rule set until all of the severity 1 alerts on the parent clear.  This value must match the format `${check_id}_${metric_name}`.

`MetricName` - (Required) The name of the metric stream within a given check that this rule set is active on.

`Tags` - (Optional) A list of tags assigned to this rule set.


## See Also

* [circonus_rule_set](https://www.terraform.io/docs/providers/circonus/r/rule_set.html) in the _Terraform Provider Documentation_
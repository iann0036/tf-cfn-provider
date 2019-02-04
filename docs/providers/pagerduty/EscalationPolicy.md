# Terraform::PagerDuty::EscalationPolicy

An [escalation policy](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Escalation_Policies/get_escalation_policies) determines what user or schedule will be notified first, second, and so on when an incident is triggered. Escalation policies are used by one or more services.

## Properties

`Name` - (Required) The name of the escalation policy.

`Teams` - (Optional) Teams associated with the policy. Account must have the `Teams` ability to use this parameter.

`Description` - (Optional) A human-friendly description of the escalation policy.
If not set, a placeholder of "Managed by Terraform" will be set.

`NumLoops` - (Optional) The number of times the escalation policy will repeat after reaching the end of its escalation.

`Rule` - (Required) An Escalation rule block. Escalation rules documented below.

### Rule Properties

`EscalationDelayInMinutes` - (Required) The number of minutes before an unacknowledged incident escalates away from this rule.

`Targets` - (Required) A target block. Target blocks documented below.

`Type` - (Optional) Can be `user`, `schedule`, `user_reference` or `schedule_reference`. Defaults to `user_reference`.

`Id` - (Required) A target ID.


## Return Values

### Fn::GetAtt

`Id` - The ID of the escalation policy.

## See Also

* [pagerduty_escalation_policy](https://www.terraform.io/docs/providers/pagerduty/r/escalation_policy.html) in the _Terraform Provider Documentation_
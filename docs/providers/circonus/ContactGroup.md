# Terraform::Circonus::ContactGroup

The ``Terraform::Circonus::ContactGroup`` resource creates and manages a
[Circonus Contact Group](https://login.circonus.com/user/docs/Alerting/ContactGroups).

## Properties

`AggregationWindow` - (Optional) The aggregation window for batching up alert notifications.

`AlertOption` - (Optional) There is one `AlertOption` per severity, where severity can be any number between 1 (high) and 5 (low).  If configured, the alerting system will remind or escalate alerts to further contact groups if an alert sent to this contact group is not acknowledged or resolved.  See below for details.

`Email` - (Optional) Zero or more `Email` attributes may be present to dispatch email to Circonus users by referencing their user ID, or by specifying an email address.  See below for details on supported attributes.

`Http` - (Optional) Zero or more `Http` attributes may be present to dispatch [Webhook/HTTP requests](https://login.circonus.com/user/docs/Alerting/ContactGroups#WebhookNotifications) by Circonus.  See below for details on supported attributes.

`Irc` - (Optional) Zero or more `Irc` attributes may be present to dispatch IRC notifications to users.  See below for details on supported attributes.

`LongMessage` - (Optional) The bulk of the message used in long form alert messages.

`LongSubject` - (Optional) The subject used in long form alert messages.

`LongSummary` - (Optional) The brief summary used in long form alert messages.

`Name` - (Required) The name of the contact group.

`PagerDuty` - (Optional) Zero or more `PagerDuty` attributes may be present to dispatch to [Pager Duty teams](https://login.circonus.com/user/docs/Alerting/ContactGroups#PagerDutyOptions). See below for details on supported attributes.

`ShortMessage` - (Optional) The subject used in short form alert messages.

`ShortSummary` - (Optional) The brief summary used in short form alert messages.

`Slack` - (Optional) Zero or more `Slack` attributes may be present to dispatch to Slack teams.  See below for details on supported attributes.

`Sms` - (Optional) Zero or more `Sms` attributes may be present to dispatch SMS messages to Circonus users by referencing their user ID, or by specifying an SMS Phone Number.  See below for details on supported attributes.

`Tags` - (Optional) A list of tags attached to the Contact Group.

`Victorops` - (Optional) Zero or more `Victorops` attributes may be present to dispatch to [VictorOps teams](https://login.circonus.com/user/docs/Alerting/ContactGroups#VictorOps). See below for details on supported attributes.


## See Also

* [circonus_contact_group](https://www.terraform.io/docs/providers/circonus/r/contact_group.html) in the _Terraform Provider Documentation_
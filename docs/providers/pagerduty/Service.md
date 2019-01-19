# Terraform::PagerDuty::Service

A [service](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services) represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.

## Properties

`Name` - Designates either the start or the end of the scheduled action. Can be `support_hours_start` or `support_hours_end`.

`Description` - (Optional) A human-friendly description of the service. If not set, a placeholder of "Managed by Terraform" will be set. * `AutoResolveTimeout` - (Optional) Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the `"null"` string. * `AcknowledgementTimeout` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `"null"` string. * `EscalationPolicy` - (Required) The escalation policy used by this service. * `AlertCreation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.

`AutoResolveTimeout` - (Optional) Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the `"null"` string. * `AcknowledgementTimeout` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `"null"` string. * `EscalationPolicy` - (Required) The escalation policy used by this service. * `AlertCreation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.

`AcknowledgementTimeout` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `"null"` string. * `EscalationPolicy` - (Required) The escalation policy used by this service. * `AlertCreation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.

`EscalationPolicy` - (Required) The escalation policy used by this service. * `AlertCreation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.

`AlertCreation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.

`Type` - The type of time specification. Currently, this must be set to `named_time`. * `Name` - Designates either the start or the end of the scheduled action. Can be `support_hours_start` or `support_hours_end`.

`Urgency` - The urgency: `low` (does not escalate), or `high` (follows escalation rules). * `DuringSupportHours` - (Optional) Incidents' urgency during support hours. * `OutsideSupportHours` - (Optional) Incidents' urgency outside of support hours.

`DuringSupportHours` - (Optional) Incidents' urgency during support hours. * `OutsideSupportHours` - (Optional) Incidents' urgency outside of support hours.

`OutsideSupportHours` - (Optional) Incidents' urgency outside of support hours.

`TimeZone` - The time zone for the support hours. * `DaysOfWeek` - Array of days of week as integers. `1` to `7`, `1` being Monday and `7` being Sunday. * `StartTime` - The support hours' starting time of day. * `EndTime` - The support hours' ending time of day.

`DaysOfWeek` - Array of days of week as integers. `1` to `7`, `1` being Monday and `7` being Sunday. * `StartTime` - The support hours' starting time of day. * `EndTime` - The support hours' ending time of day.

`StartTime` - The support hours' starting time of day. * `EndTime` - The support hours' ending time of day.

`EndTime` - The support hours' ending time of day.

`ToUrgency` - The urgency to change to: `low` (does not escalate), or `high` (follows escalation rules). * `At` - A block representing when the scheduled action will occur.

`At` - A block representing when the scheduled action will occur.


## Return Values

### Fn::GetAtt

`Id` - The ID of the service.

`LastIncidentTimestamp` - Last incident timestamp of the service.

`CreatedAt` - Creation timestamp of the service.

`Status` - The status of the service.

## See Also

* [pagerduty_service](https://www.terraform.io/docs/providers/pagerduty/r/service.html) in the _Terraform Provider Documentation_
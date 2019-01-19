# Terraform::PagerDuty::Service

A [service](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services) represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the service.

`LastIncidentTimestamp` - Last incident timestamp of the service.

`CreatedAt` - Creation timestamp of the service.

`Status` - The status of the service.

## See Also

* [pagerduty_service](https://www.terraform.io/docs/providers/pagerduty/r/service.html) in the _Terraform Provider Documentation_
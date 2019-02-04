# Terraform::PagerDuty::ServiceIntegration

A [service integration](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/post_services_id_integrations) is an integration that belongs to a service.

## Properties

`Service` - (Required) The ID of the service the integration should belong to.
* `Name` - (Optional) The name of the service integration.
* `Type` - (Optional) The service type. Can be:
`aws_cloudwatch_inbound_integration`,
`cloudkick_inbound_integration`,
`event_transformer_api_inbound_integration`,
`events_api_v2_inbound_integration` (requires service `alert_creation` to be `create_alerts_and_incidents`),
`generic_email_inbound_integration`,
`generic_events_api_inbound_integration`,
`keynote_inbound_integration`,
`nagios_inbound_integration`,
`pingdom_inbound_integration`or `sql_monitor_inbound_integration`.

`Name` - (Optional) The name of the service integration.
* `Type` - (Optional) The service type. Can be:
`aws_cloudwatch_inbound_integration`,
`cloudkick_inbound_integration`,
`event_transformer_api_inbound_integration`,
`events_api_v2_inbound_integration` (requires service `alert_creation` to be `create_alerts_and_incidents`),
`generic_email_inbound_integration`,
`generic_events_api_inbound_integration`,
`keynote_inbound_integration`,
`nagios_inbound_integration`,
`pingdom_inbound_integration`or `sql_monitor_inbound_integration`.

`Type` - (Optional) The service type. Can be:
`aws_cloudwatch_inbound_integration`,
`cloudkick_inbound_integration`,
`event_transformer_api_inbound_integration`,
`events_api_v2_inbound_integration` (requires service `alert_creation` to be `create_alerts_and_incidents`),
`generic_email_inbound_integration`,
`generic_events_api_inbound_integration`,
`keynote_inbound_integration`,
`nagios_inbound_integration`,
`pingdom_inbound_integration`or `sql_monitor_inbound_integration`.

`Vendor` - (Optional) The ID of the vendor the integration should integrate with (e.g Datadog or Amazon Cloudwatch).
* `IntegrationKey` - (Optional) This is the unique key used to route events to this integration when received via the PagerDuty Events API.
* `IntegrationEmail` - (Optional) This is the unique fully-qualified email address used for routing emails to this integration for processing.

`IntegrationKey` - (Optional) This is the unique key used to route events to this integration when received via the PagerDuty Events API.
* `IntegrationEmail` - (Optional) This is the unique fully-qualified email address used for routing emails to this integration for processing.

`IntegrationEmail` - (Optional) This is the unique fully-qualified email address used for routing emails to this integration for processing.


## Return Values

### Fn::GetAtt

`Id` - The ID of the service integration.

`IntegrationKey` - This is the unique key used to route events to this integration when received via the PagerDuty Events API.

`IntegrationEmail` - This is the unique fully-qualified email address used for routing emails to this integration for processing.

`HtmlUrl` - URL at which the entity is uniquely displayed in the Web app.

## See Also

* [pagerduty_service_integration](https://www.terraform.io/docs/providers/pagerduty/r/service_integration.html) in the _Terraform Provider Documentation_
# Terraform::PagerDuty::ServiceIntegration

A [service integration](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/post_services_id_integrations) is an integration that belongs to a service.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the service integration.

`IntegrationKey` - This is the unique key used to route events to this integration when received via the PagerDuty Events API.

`IntegrationEmail` - This is the unique fully-qualified email address used for routing emails to this integration for processing.

`HtmlUrl` - URL at which the entity is uniquely displayed in the Web app.

## See Also

* [pagerduty_service_integration](https://www.terraform.io/docs/providers/pagerduty/r/service_integration.html) in the _Terraform Provider Documentation_
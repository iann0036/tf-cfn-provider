# Terraform::Datadog::IntegrationPagerduty

Provides a Datadog - PagerDuty resource. This can be used to create and manage Datadog - PagerDuty integration.

## Properties

`Services` - (Optional) Array of PagerDuty service objects. * `ServiceName` - (Required) Your Service name in PagerDuty. * `ServiceKey` - (Required) Your Service name associated service key in Pagerduty.

`ServiceName` - (Required) Your Service name in PagerDuty. * `ServiceKey` - (Required) Your Service name associated service key in Pagerduty.

`ServiceKey` - (Required) Your Service name associated service key in Pagerduty.

`Schedules` - (Optional)  Array of your schedule URLs.

`Subdomain` - (Required) Your PagerDuty account’s personalized subdomain name.

`ApiToken` - (Optional) Your PagerDuty API token.


## See Also

* [datadog_integration_pagerduty](https://www.terraform.io/docs/providers/datadog/r/integration_pagerduty.html) in the _Terraform Provider Documentation_
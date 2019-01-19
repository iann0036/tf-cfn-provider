# Datadog Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/datadog**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) Datadog API key.
* `app_key` - (Required) Datadog APP key.
* `api_url` - (Optional) The API Url.


## Supported Resources

* [Terraform::Datadog::Downtime](Downtime.md)
* [Terraform::Datadog::IntegrationAws](IntegrationAws.md)
* [Terraform::Datadog::IntegrationGcp](IntegrationGcp.md)
* [Terraform::Datadog::IntegrationPagerduty](IntegrationPagerduty.md)
* [Terraform::Datadog::MetricMetadata](MetricMetadata.md)
* [Terraform::Datadog::Monitor](Monitor.md)
* [Terraform::Datadog::Screenboard](Screenboard.md)
* [Terraform::Datadog::Timeboard](Timeboard.md)
* [Terraform::Datadog::User](User.md)
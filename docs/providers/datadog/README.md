# Datadog Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/datadog**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) Datadog API key.
* `app_key` - (Required) Datadog APP key.
* `api_url` - (Optional) The API Url.


## Supported Resources

* [Terraform::Datadog::Downtime](docs/providers/datadog/Downtime.md)
* [Terraform::Datadog::IntegrationAws](docs/providers/datadog/IntegrationAws.md)
* [Terraform::Datadog::IntegrationGcp](docs/providers/datadog/IntegrationGcp.md)
* [Terraform::Datadog::IntegrationPagerduty](docs/providers/datadog/IntegrationPagerduty.md)
* [Terraform::Datadog::MetricMetadata](docs/providers/datadog/MetricMetadata.md)
* [Terraform::Datadog::Monitor](docs/providers/datadog/Monitor.md)
* [Terraform::Datadog::Screenboard](docs/providers/datadog/Screenboard.md)
* [Terraform::Datadog::Timeboard](docs/providers/datadog/Timeboard.md)
* [Terraform::Datadog::User](docs/providers/datadog/User.md)
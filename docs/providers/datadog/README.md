# Datadog Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/datadog** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

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
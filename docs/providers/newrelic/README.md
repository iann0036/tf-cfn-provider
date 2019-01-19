# NewRelic Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/newrelic**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) Your New Relic API key.


## Supported Resources

* [Terraform::NewRelic::AlertChannel](docs/providers/newrelic/AlertChannel.md)
* [Terraform::NewRelic::AlertCondition](docs/providers/newrelic/AlertCondition.md)
* [Terraform::NewRelic::AlertPolicyChannel](docs/providers/newrelic/AlertPolicyChannel.md)
* [Terraform::NewRelic::AlertPolicy](docs/providers/newrelic/AlertPolicy.md)
* [Terraform::NewRelic::Dashboard](docs/providers/newrelic/Dashboard.md)
* [Terraform::NewRelic::InfraAlertCondition](docs/providers/newrelic/InfraAlertCondition.md)
* [Terraform::NewRelic::NrqlAlertCondition](docs/providers/newrelic/NrqlAlertCondition.md)
* [Terraform::NewRelic::SyntheticsAlertCondition](docs/providers/newrelic/SyntheticsAlertCondition.md)
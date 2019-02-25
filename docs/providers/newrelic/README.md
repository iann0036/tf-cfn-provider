# NewRelic Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/newrelic** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) Your New Relic API key.


## Supported Resources

* [Terraform::NewRelic::AlertChannel](AlertChannel.md)
* [Terraform::NewRelic::AlertCondition](AlertCondition.md)
* [Terraform::NewRelic::AlertPolicyChannel](AlertPolicyChannel.md)
* [Terraform::NewRelic::AlertPolicy](AlertPolicy.md)
* [Terraform::NewRelic::Dashboard](Dashboard.md)
* [Terraform::NewRelic::InfraAlertCondition](InfraAlertCondition.md)
* [Terraform::NewRelic::NrqlAlertCondition](NrqlAlertCondition.md)
* [Terraform::NewRelic::SyntheticsAlertCondition](SyntheticsAlertCondition.md)
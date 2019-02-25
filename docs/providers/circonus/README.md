# Circonus Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/circonus** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `key` - (Required) The Circonus API Key.
* `api_url` - (Optional) The API URL to use to talk with. The default is `https://api.circonus.com/v2`.


## Supported Resources

* [Terraform::Circonus::Check](Check.md)
* [Terraform::Circonus::ContactGroup](ContactGroup.md)
* [Terraform::Circonus::Graph](Graph.md)
* [Terraform::Circonus::MetricCluster](MetricCluster.md)
* [Terraform::Circonus::Metric](Metric.md)
* [Terraform::Circonus::RuleSet](RuleSet.md)
* [Terraform::Circonus::Worksheet](Worksheet.md)
# Circonus Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/circonus**. The below arguments may be included as the key/value or JSON properties in the secret:

* `key` - (Required) The Circonus API Key. It can be sourced from the `CIRCONUS_API_KEY` environment variable.
* `api_url` - (Optional) The API URL to use to talk with. The default is `https://api.circonus.com/v2`. It can be sourced from the `CIRCONUS_API_URL` environment variable.


## Supported Resources

* [Terraform::Circonus::Check](docs/providers/circonus/Check.md)
* [Terraform::Circonus::ContactGroup](docs/providers/circonus/ContactGroup.md)
* [Terraform::Circonus::Graph](docs/providers/circonus/Graph.md)
* [Terraform::Circonus::MetricCluster](docs/providers/circonus/MetricCluster.md)
* [Terraform::Circonus::Metric](docs/providers/circonus/Metric.md)
* [Terraform::Circonus::RuleSet](docs/providers/circonus/RuleSet.md)
* [Terraform::Circonus::Worksheet](docs/providers/circonus/Worksheet.md)
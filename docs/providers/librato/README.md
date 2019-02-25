# Librato Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/librato** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) Librato API token.
* `email` - (Required) Librato email address.


## Supported Resources

* [Terraform::Librato::Alert](Alert.md)
* [Terraform::Librato::Metric](Metric.md)
* [Terraform::Librato::Service](Service.md)
* [Terraform::Librato::SpaceChart](SpaceChart.md)
* [Terraform::Librato::Space](Space.md)
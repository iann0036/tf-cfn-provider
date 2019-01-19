# Librato Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/librato**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) Librato API token. It must be provided, but it can also
  be sourced from the `LIBRATO_TOKEN` environment variable.
* `email` - (Required) Librato email address. It must be provided, but it can
  also be sourced from the `LIBRATO_EMAIL` environment variable.


## Supported Resources

* [Terraform::Librato::Alert](docs/providers/librato/Alert.md)
* [Terraform::Librato::Metric](docs/providers/librato/Metric.md)
* [Terraform::Librato::Service](docs/providers/librato/Service.md)
* [Terraform::Librato::SpaceChart](docs/providers/librato/SpaceChart.md)
* [Terraform::Librato::Space](docs/providers/librato/Space.md)
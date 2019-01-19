# Atlas Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/atlas**. The below arguments may be included as the key/value or JSON properties in the secret:

* `address` - (Optional) Atlas server endpoint. Defaults to
  public Atlas. This is only required when using an on-premise
  deployment of Atlas. This can also be specified with the
  `ATLAS_ADDRESS` shell environment variable.

* `token` - (Required) API token. This can also be specified with the
  `ATLAS_TOKEN` shell environment variable.


## Supported Resources

* [Terraform::Atlas::Artifact](docs/providers/atlas/Artifact.md)
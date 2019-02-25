# Atlas Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/atlas** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `address` - (Optional) Atlas server endpoint. Defaults to
  public Atlas. This is only required when using an on-premise
  deployment of Atlas.

* `token` - (Required) API token.


## Supported Resources

* [Terraform::Atlas::Artifact](Artifact.md)
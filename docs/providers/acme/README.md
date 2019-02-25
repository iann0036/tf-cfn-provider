# ACME Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/acme** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `server_url` - (Required) The URL to the ACME endpoint's directory.

-> Note that the account key is not a provider-level config value at this time
to allow the management of accounts and certificates within the same provider.


## Supported Resources

* [Terraform::ACME::Certificate](Certificate.md)
* [Terraform::ACME::Registration](Registration.md)
# ACME Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/acme**. The below arguments may be included as the key/value or JSON properties in the secret:

* `server_url` - (Required) The URL to the ACME endpoint's directory.

-> Note that the account key is not a provider-level config value at this time
to allow the management of accounts and certificates within the same provider.


## Supported Resources

* [Terraform::ACME::Certificate](docs/providers/acme/Certificate.md)
* [Terraform::ACME::Registration](docs/providers/acme/Registration.md)
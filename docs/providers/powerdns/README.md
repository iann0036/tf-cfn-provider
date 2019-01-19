# PowerDNS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/powerdns**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) The PowerDNS API key.
* `server_url` - (Required) The address of PowerDNS server.


## Supported Resources

* [Terraform::PowerDNS::Record](docs/providers/powerdns/Record.md)
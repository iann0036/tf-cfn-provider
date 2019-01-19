# NS1 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ns1**. The below arguments may be included as the key/value or JSON properties in the secret:

* `apikey` - (Required) NS1 API token. It must be provided, but it can also
  be sourced from the `NS1_APIKEY` environment variable.



## Supported Resources

* [Terraform::NS1::Apikey](docs/providers/ns1/Apikey.md)
* [Terraform::NS1::Datafeed](docs/providers/ns1/Datafeed.md)
* [Terraform::NS1::Datasource](docs/providers/ns1/Datasource.md)
* [Terraform::NS1::Monitoringjob](docs/providers/ns1/Monitoringjob.md)
* [Terraform::NS1::Notifylist](docs/providers/ns1/Notifylist.md)
* [Terraform::NS1::Record](docs/providers/ns1/Record.md)
* [Terraform::NS1::Team](docs/providers/ns1/Team.md)
* [Terraform::NS1::User](docs/providers/ns1/User.md)
* [Terraform::NS1::Zone](docs/providers/ns1/Zone.md)
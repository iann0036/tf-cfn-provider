# NS1 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ns1** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `apikey` - (Required) NS1 API token.



## Supported Resources

* [Terraform::NS1::Apikey](Apikey.md)
* [Terraform::NS1::Datafeed](Datafeed.md)
* [Terraform::NS1::Datasource](Datasource.md)
* [Terraform::NS1::Monitoringjob](Monitoringjob.md)
* [Terraform::NS1::Notifylist](Notifylist.md)
* [Terraform::NS1::Record](Record.md)
* [Terraform::NS1::Team](Team.md)
* [Terraform::NS1::User](User.md)
* [Terraform::NS1::Zone](Zone.md)
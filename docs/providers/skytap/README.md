# Skytap Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/skytap** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `username` - (Required) This is the Skytap username.
* `api_token` - (Required) This is the Skytap API token.





## Supported Resources

* [Terraform::Skytap::Environment](Environment.md)
* [Terraform::Skytap::Network](Network.md)
* [Terraform::Skytap::Project](Project.md)
* [Terraform::Skytap::Vm](Vm.md)
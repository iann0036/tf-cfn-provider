# Skytap Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/skytap**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) This is the Skytap username. This can also be specified
  with the `SKYTAP_USERNAME` shell environment variable.
* `api_token` - (Required) This is the Skytap API token. This can also be specified
  with the `SKYTAP_API_TOKEN` shell environment variable.





## Supported Resources

* [Terraform::Skytap::Environment](docs/providers/skytap/Environment.md)
* [Terraform::Skytap::Network](docs/providers/skytap/Network.md)
* [Terraform::Skytap::Project](docs/providers/skytap/Project.md)
* [Terraform::Skytap::Vm](docs/providers/skytap/Vm.md)
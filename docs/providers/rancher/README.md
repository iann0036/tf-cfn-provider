# Rancher Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rancher**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_url` - (Required) Rancher API url. It must be provided, but it can also be sourced from the `RANCHER_URL` environment variable.
* `access_key` - (Optional) Rancher API access key. It can also be sourced from the `RANCHER_ACCESS_KEY` environment variable.
* `secret_key` - (Optional) Rancher API access key. It can also be sourced from the `RANCHER_SECRET_KEY` environment variable.


## Supported Resources

* [Terraform::Rancher::Certificate](docs/providers/rancher/Certificate.md)
* [Terraform::Rancher::Environment](docs/providers/rancher/Environment.md)
* [Terraform::Rancher::Host](docs/providers/rancher/Host.md)
* [Terraform::Rancher::RegistrationToken](docs/providers/rancher/RegistrationToken.md)
* [Terraform::Rancher::RegistryCredential](docs/providers/rancher/RegistryCredential.md)
* [Terraform::Rancher::Registry](docs/providers/rancher/Registry.md)
* [Terraform::Rancher::Secrets](docs/providers/rancher/Secrets.md)
* [Terraform::Rancher::Stack](docs/providers/rancher/Stack.md)
* [Terraform::Rancher::Volumes](docs/providers/rancher/Volumes.md)
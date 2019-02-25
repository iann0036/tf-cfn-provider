# Rancher Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rancher** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_url` - (Required) Rancher API url.
* `access_key` - (Optional) Rancher API access key.
* `secret_key` - (Optional) Rancher API access key.


## Supported Resources

* [Terraform::Rancher::Certificate](Certificate.md)
* [Terraform::Rancher::Environment](Environment.md)
* [Terraform::Rancher::Host](Host.md)
* [Terraform::Rancher::RegistrationToken](RegistrationToken.md)
* [Terraform::Rancher::RegistryCredential](RegistryCredential.md)
* [Terraform::Rancher::Registry](Registry.md)
* [Terraform::Rancher::Secrets](Secrets.md)
* [Terraform::Rancher::Stack](Stack.md)
* [Terraform::Rancher::Volumes](Volumes.md)
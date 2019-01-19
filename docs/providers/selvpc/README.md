# Selectel Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/selvpc**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) The Selectel API key token. If omitted, the `SEL_TOKEN`
  environment variable is used.

* `endpoint` - (Optional) The Selectel VPC endpoint. Needed only if this provider
  is used for tests environment. If omitted, the provider will use the official
  Selectel VPC endpoint automatically.


## Supported Resources

* [Terraform::SelVPC::ResellFloatingipV2](docs/providers/selvpc/ResellFloatingipV2.md)
* [Terraform::SelVPC::ResellKeypairV2](docs/providers/selvpc/ResellKeypairV2.md)
* [Terraform::SelVPC::ResellLicenseV2](docs/providers/selvpc/ResellLicenseV2.md)
* [Terraform::SelVPC::ResellProjectV2](docs/providers/selvpc/ResellProjectV2.md)
* [Terraform::SelVPC::ResellRoleV2](docs/providers/selvpc/ResellRoleV2.md)
* [Terraform::SelVPC::ResellSubnetV2](docs/providers/selvpc/ResellSubnetV2.md)
* [Terraform::SelVPC::ResellTokenV2](docs/providers/selvpc/ResellTokenV2.md)
* [Terraform::SelVPC::ResellUserV2](docs/providers/selvpc/ResellUserV2.md)
* [Terraform::SelVPC::ResellVrrpSubnetV2](docs/providers/selvpc/ResellVrrpSubnetV2.md)
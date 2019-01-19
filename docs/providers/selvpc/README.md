# Selectel Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/selvpc**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) The Selectel API key token.

* `endpoint` - (Optional) The Selectel VPC endpoint. Needed only if this provider
  is used for tests environment. If omitted, the provider will use the official
  Selectel VPC endpoint automatically.


## Supported Resources

* [Terraform::SelVPC::ResellFloatingipV2](ResellFloatingipV2.md)
* [Terraform::SelVPC::ResellKeypairV2](ResellKeypairV2.md)
* [Terraform::SelVPC::ResellLicenseV2](ResellLicenseV2.md)
* [Terraform::SelVPC::ResellProjectV2](ResellProjectV2.md)
* [Terraform::SelVPC::ResellRoleV2](ResellRoleV2.md)
* [Terraform::SelVPC::ResellSubnetV2](ResellSubnetV2.md)
* [Terraform::SelVPC::ResellTokenV2](ResellTokenV2.md)
* [Terraform::SelVPC::ResellUserV2](ResellUserV2.md)
* [Terraform::SelVPC::ResellVrrpSubnetV2](ResellVrrpSubnetV2.md)
# Terraform::Vault::AwsAuthBackendStsRole

Manages an STS role in a Vault server. STS roles are mappings
between account IDs and STS ARNs. When a login attempt is made
from an EC2 instance in the account ID specified, the associated
STS role will be used to verify the request. For more information,
see the [Vault documentation](https://www.vaultproject.io/docs/auth/aws.html#cross-account-access).

~> **Important** All data provided in the resource configuration will be
 written in cleartext to state and plan files generated by Terraform, and will
 appear in the console output when Terraform runs. Protect these artifacts
 accordingly. See [the main provider documentation](../../index.html) for more
 details.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [vault_aws_auth_backend_sts_role](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_sts_role.html) in the _Terraform Provider Documentation_
# Terraform::Vault::AwsAuthBackendRoleTag

Reads role tag information from an AWS auth backend in Vault.

## Properties

`Role` - (Required) The name of the AWS auth backend role to read
role tags from, with no leading or trailing `/`s.

`Backend` - (Optional) The path to the AWS auth backend to
read role tags from, with no leading or trailing `/`s. Defaults to "aws".

`Policies` - (Optional) The policies to be associated with the tag. Must be a subset of the policies associated with the role.

`MaxTtl` - (Optional) The maximum TTL of the tokens issued using this role.

`InstanceId` - (Optional) Instance ID for which this tag is intended for. If set, the created tag can only be used by the instance with the given ID.

`AllowInstanceMigration` - (Optional) If set, allows migration of the underlying instances where the client resides. Use with caution.

`DisallowReauthentication` - (Optional) If set, only allows a single token to be granted per instance ID.


## Return Values

### Fn::GetAtt

`TagKey` - The key of the role tag.

`TagValue` - The value to set the role key.

## See Also

* [vault_aws_auth_backend_role_tag](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role_tag.html) in the _Terraform Provider Documentation_
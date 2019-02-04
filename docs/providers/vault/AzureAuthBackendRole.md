# Terraform::Vault::AzureAuthBackendRole

Manages an Azure auth backend role in a Vault server. Roles constrain the
instances or principals that can perform the login operation against the
backend. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/azure.html) for more
information.

## Properties

`Role` - (Required) The name of the role.

`BoundServicePrincipalIds` - (Optional) If set, defines a constraint on the
service principals that can perform the login operation that they should be posess
the ids specified by this field.

`BoundGroupIds` - (Optional) If set, defines a constraint on the groups
that can perform the login operation that they should be using the group
ID specified by this field.

`BoundLocations` - (Optional) If set, defines a constraint on the virtual machines
that can perform the login operation that the location in their identity
document must match the one specified by this field.

`BoundSubscriptionIds` - (Optional) If set, defines a constraint on the subscriptions
that can perform the login operation to ones which  matches the value specified by this
field.

`BoundResourceGroups` - (Optional) If set, defines a constraint on the virtual
machiness that can perform the login operation that they be associated with
the resource group that matches the value specified by this field.

`BoundScaleSets` - (Optional) If set, defines a constraint on the virtual
machines that can perform the login operation that they must match the scale set
specified by this field.

`Ttl` - (Optional) The TTL period of tokens issued using this role, provided
as a number of seconds.

`MaxTtl` - (Optional) The maximum allowed lifetime of tokens issued using
this role, provided as a number of seconds.

`Period` - (Optional) If set, indicates that the token generated using this
role should never expire. The token should be renewed within the duration
specified by this value. At each renewal, the token's TTL will be set to the
value of this field. The maximum allowed lifetime of token issued using this
role. Specified as a number of seconds.

`Policies` - (Optional) An array of strings specifying the policies to be set
on tokens issued using this role.


## See Also

* [vault_azure_auth_backend_role](https://www.terraform.io/docs/providers/vault/r/azure_auth_backend_role.html) in the _Terraform Provider Documentation_
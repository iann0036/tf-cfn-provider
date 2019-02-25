# Terraform::Vault::IdentityGroup

Creates an Identity Group for Vault. The [Identity secrets engine](https://www.vaultproject.io/docs/secrets/identity/index.html) is the identity management solution for Vault.

A group can contain multiple entities as its members. A group can also have subgroups. Policies set on the group is granted to all members of the group. During request time, when the token's entity ID is being evaluated for the policies that it has access to; along with the policies on the entity itself, policies that are inherited due to group memberships are also granted.

## Properties

`Name` - (Required, Forces new resource) Name of the identity group to create.

`Type` - (Optional, Forces new resource) Type of the group, internal or external. Defaults to `internal`.

`Policies` - (Optional) A list of policies to apply to the group.

`Metadata` - (Optional) A Map of additional metadata to associate with the group.

`MemberGroupIds` - (Optional) A list of Group IDs to be assigned as group members.

`MemberEntityIds` - (Optional) A list of Entity IDs to be assigned as group members. Not allowed on `external` groups.


## Return Values

### Fn::GetAtt

`Id` - The `id` of the created group.

## See Also

* [vault_identity_group](https://www.terraform.io/docs/providers/vault/r/identity_group.html) in the _Terraform Provider Documentation_
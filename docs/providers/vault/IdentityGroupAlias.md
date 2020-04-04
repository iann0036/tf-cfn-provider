# Terraform::Vault::IdentityGroupAlias

Creates an Identity Group Alias for Vault. The [Identity secrets engine](https://www.vaultproject.io/docs/secrets/identity/index.html) is the identity management solution for Vault.

Group aliases allows entity membership in external groups to be managed semi-automatically. External group serves as a mapping to a group that is outside of the identity store. External groups can have one (and only one) alias. This alias should map to a notion of group that is outside of the identity store. For example, groups in LDAP, and teams in GitHub. A username in LDAP, belonging to a group in LDAP, can get its entity ID added as a member of a group in Vault automatically during logins and token renewals. This works only if the group in Vault is an external group and has an alias that maps to the group in LDAP. If the user is removed from the group in LDAP, that change gets reflected in Vault only upon the subsequent login or renewal operation.

## Properties

`Name` - (Required, Forces new resource) Name of the group alias to create.

`MountAccessor` - (Required) Mount accessor of the authentication backend to which this alias belongs to.

`CanonicalId` - (Required) ID of the group to which this is an alias.


## Return Values

### Fn::GetAtt

`Id` - The `id` of the created group alias.

## See Also

* [vault_identity_group_alias](https://www.terraform.io/docs/providers/vault/r/identity_group_alias.html) in the _Terraform Provider Documentation_
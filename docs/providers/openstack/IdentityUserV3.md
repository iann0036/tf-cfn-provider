# Terraform::OpenStack::IdentityUserV3

Manages a V3 User resource within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

## Properties

`Description` - (Optional) A description of the user.

`DefaultProjectId` - (Optional) The default project this user belongs to.

`DomainId` - (Optional) The domain this user belongs to.

`Enabled` - (Optional) Whether the user is enabled or disabled. Valid values are `true` and `false`.

`Extra` - (Optional) Free-form key/value pairs of extra information.

`IgnoreChangePasswordUponFirstUse` - (Optional) User will not have to change their password upon first use. Valid values are `true` and `false`.

`IgnorePasswordExpiry` - (Optional) User's password will not expire. Valid values are `true` and `false`.

`IgnoreLockoutFailureAttempts` - (Optional) User will not have a failure lockout placed on their account. Valid values are `true` and `false`.

`MultiFactorAuthEnabled` - (Optional) Whether to enable multi-factor authentication. Valid values are `true` and `false`.

`MultiFactorAuthRule` - (Optional) A multi-factor authentication rule. The structure is documented below. Please see the [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html) for more information on how to use mulit-factor rules.

`Name` - (Optional) The name of the user.

`Password` - (Optional) The password for the user.

`Region` - (Optional) The region in which to obtain the V3 Keystone client. If omitted, the `Region` argument of the provider is used. Changing this creates a new User.

`Rule` - (Required) A list of authentication plugins that the user must authenticate with.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

## See Also

* [openstack_identity_user_v3](https://www.terraform.io/docs/providers/openstack/r/identity_user_v3.html) in the _Terraform Provider Documentation_
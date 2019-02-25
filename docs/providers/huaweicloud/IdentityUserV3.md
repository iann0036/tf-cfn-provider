# Terraform::HuaweiCloud::IdentityUserV3

Manages a User resource within HuaweiCloud IAM service.

Note: You _must_ have admin privileges in your HuaweiCloud cloud to use
this resource.

## Properties

`Name` - (Required) The name of the user. The user name consists of 5 to 32
characters. It can contain only uppercase letters, lowercase letters,
digits, spaces, and special characters (-_) and cannot start with a digit.

`Description` - (Optional) A description of the user.

`DefaultProjectId` - (Optional) The default project this user belongs to.

`DomainId` - (Optional) The domain this user belongs to.

`Enabled` - (Optional) Whether the user is enabled or disabled. Valid
values are `true` and `false`.

`Password` - (Optional) The password for the user. It must contain at least
two of the following character types: uppercase letters, lowercase letters,
digits, and special characters.

`Region` - (Optional) The region in which to obtain the V3 Keystone client.
If omitted, the `Region` argument of the provider is used. Changing this
creates a new User.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

## See Also

* [huaweicloud_identity_user_v3](https://www.terraform.io/docs/providers/huaweicloud/r/identity_user_v3.html) in the _Terraform Provider Documentation_
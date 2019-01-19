# Terraform::Cloudflare::AccountMember

Provides a resource which manages Cloudflare account members.

## Properties

`EmailAddress` - (Required) The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.

`RoleIds` - (Required) Array of account role IDs that you want to assign to a member.


## See Also

* [cloudflare_account_member](https://www.terraform.io/docs/providers/cloudflare/r/account_member.html) in the _Terraform Provider Documentation_
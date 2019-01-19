# Terraform::Alicloud::RamUser

Provides a RAM User resource.

~> **NOTE:** When you want to destroy this resource forcefully(means release all the relationships associated with it automatically and then destroy it) without set `force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The user ID.

`Name` - The user name.

`DisplayName` - The user display name.

`Mobile` - The user phone number.

`Email` - The user email.

`Comments` - The user comments.

## See Also

* [alicloud_ram_user](https://www.terraform.io/docs/providers/alicloud/r/ram_user.html) in the _Terraform Provider Documentation_
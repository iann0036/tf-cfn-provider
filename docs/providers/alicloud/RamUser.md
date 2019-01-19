# Terraform::Alicloud::RamUser

Provides a RAM User resource.

~> **NOTE:** When you want to destroy this resource forcefully(means release all the relationships associated with it automatically and then destroy it) without set `Force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Properties

`Name` - (Required) Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.

`DisplayName` - (Optional) Name of the RAM user which for display. This name can have a string of 1 to 12 characters or Chinese characters, must contain only alphanumeric characters or Chinese characters or hyphens, such as "-",".", and must not end with a hyphen.

`Mobile` - (Optional) Phone number of the RAM user. This number must contain an international area code prefix, just look like this: 86-18600008888.

`Email` - (Optional) Email of the RAM user.

`Comments` - (Optional) Comment of the RAM user. This parameter can have a string of 1 to 128 characters.

`Force` - (Optional) This parameter is used for resource destroy. Default value is `false`.


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
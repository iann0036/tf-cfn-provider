# Terraform::Alicloud::RamRole

Provides a RAM Role resource.

~> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `Force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Properties

`Name` - (Required, Forces new resource) Name of the RAM role. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-", "_", and must not begin with a hyphen.

`Services` - (Optional, Type: list, Conflicts with `Document`) List of services which can assume the RAM role. The format of each item in this list is `${service}.aliyuncs.com` or `${account_id}@${service}.aliyuncs.com`, such as `ecs.aliyuncs.com` and `1234567890000@ots.aliyuncs.com`. The `${service}` can be `ecs`, `log`, `apigateway` and so on, the `${account_id}` refers to someone's Alicloud account id.

`RamUsers` - (Optional, Type: list, Conflicts with `Document`) List of ram users who can assume the RAM role. The format of each item in this list is `acs:ram::${account_id}:root` or `acs:ram::${account_id}:user/${user_name}`, such as `acs:ram::1234567890000:root` and `acs:ram::1234567890001:user/Mary`. The `${user_name}` is the name of a RAM user which must exists in the Alicloud account indicated by the `${account_id}`.

`Version` - (Optional, Conflicts with `Document`) Version of the RAM role policy document. Valid value is `1`. Default value is `1`.

`Document` - (Optional, Conflicts with `Services`, `RamUsers` and `Version`) Authorization strategy of the RAM role. It is required when the `Services` and `RamUsers` are not specified.

`Description` - (Optional, Forces new resource) Description of the RAM role. This name can have a string of 1 to 1024 characters.

`Force` - (Optional) This parameter is used for resource destroy. Default value is `false`.


## Return Values

### Fn::GetAtt

`Id` - The role ID.

`Name` - The role name.

`Arn` - The role arn.

`Description` - The role description.

`Version` - The role policy document version.

`Document` - Authorization strategy of the role.

`RamUsers` - List of services which can assume the RAM role.

`Services` - List of services which can assume the RAM role.

## See Also

* [alicloud_ram_role](https://www.terraform.io/docs/providers/alicloud/r/ram_role.html) in the _Terraform Provider Documentation_
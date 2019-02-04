# Terraform::Alicloud::RamPolicy

Provides a RAM Policy resource. 

~> **NOTE:** When you want to destroy this resource forcefully(means remove all the relationships associated with it automatically and then destroy it) without set `Force`  with `true` at beginning, you need add `force = true` to configuration file and run `terraform plan`, then you can delete resource forcefully.

## Properties

`Name` - (Required, Forces new resource) Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.

`Statement` - (Optional,  Type: list, Conflicts with `Document`) Statements of the RAM policy document. It is required when the `Document` is not specified.

`Resource` - (Required, Type: list) List of specific objects which will be authorized. The format of each item in this list is `acs:${service}:${region}:${account_id}:${relative_id}`, such as `acs:ecs:*:*:instance/inst-002` and `acs:oss:*:1234567890000:mybucket`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${region}` is the region info which can use `*` replace when it is not supplied, the `${account_id}` refers to someone's Alicloud account id or you can use `*` to replace, the `${relative_id}` is the resource description section which related to the `${service}`.

`Action` - (Required, Type: list) List of operations for the `Resource`. The format of each item in this list is `${service}:${action_name}`, such as `oss:ListBuckets` and `ecs:Describe*`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${action_name}` refers to the name of an api interface which related to the `${service}`.

`Effect` - (Required) This parameter indicates whether or not the `Action` is allowed. Valid values are `Allow` and `Deny`.

`Version` - (Optional, Conflicts with `Document`) Version of the RAM policy document. Valid value is `1`. Default value is `1`.

`Document` - (Optional, Conflicts with `Statement` and `Version`) Document of the RAM policy. It is required when the `Statement` is not specified.

`Description` - (Optional, Forces new resource) Description of the RAM policy. This name can have a string of 1 to 1024 characters.

`Force` - (Optional) This parameter is used for resource destroy. Default value is `false`.


## Return Values

### Fn::GetAtt

`Id` - The policy ID.

`Name` - The policy name.

`Type` - The policy type.

`Description` - The policy description.

`Statement` - List of statement of the policy document.

`Document` - The policy document.

`Version` - The policy document version.

`AttachmentCount` - The policy attachment count.

## See Also

* [alicloud_ram_policy](https://www.terraform.io/docs/providers/alicloud/r/ram_policy.html) in the _Terraform Provider Documentation_
# Terraform::Datadog::User

Provides a Datadog user resource. This can be used to create and manage Datadog users.

## Properties

`Disabled` - (Optional) Whether the user is disabled.

`Email` - (Required) Email address for user.

`Handle` - (Required) The user handle, must be a valid email.

`IsAdmin` - (Deprecated) (Optional) Whether the user is an administrator.

`Name` - (Required) Name for user.

`Role` - (Deprecated) Role description for user. **Warning**: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.


## Return Values

### Fn::GetAtt

`Disabled` - Returns true if Datadog user is disabled (NOTE: Datadog does not actually delete users so this will be true for those as well).

`Id` - ID of the Datadog user.

`Verified` - Returns true if Datadog user is verified.

## See Also

* [datadog_user](https://www.terraform.io/docs/providers/datadog/r/user.html) in the _Terraform Provider Documentation_
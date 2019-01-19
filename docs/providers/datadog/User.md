# Terraform::Datadog::User

Provides a Datadog user resource. This can be used to create and manage Datadog users.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Disabled` - Returns true if Datadog user is disabled (NOTE: Datadog does not actually delete users so this will be true for those as well).

`Id` - ID of the Datadog user.

`Verified` - Returns true if Datadog user is verified.

## See Also

* [datadog_user](https://www.terraform.io/docs/providers/datadog/r/user.html) in the _Terraform Provider Documentation_
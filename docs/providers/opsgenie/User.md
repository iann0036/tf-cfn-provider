# Terraform::OpsGenie::User

Manages a User within OpsGenie.

## Properties

`Username` - (Required) The email address associated with this user. OpsGenie defines that this must not be longer than 100 characters.

`FullName` - (Required) The Full Name of the User.

`Role` - (Required) The Role assigned to the User. Either a built-in such as 'Owner', 'Admin' or 'User' - or the name of a custom role.

`Locale` - (Optional) Location information for the user. Please look at [Supported Locale Ids](https://www.opsgenie.com/docs/miscellaneous/supported-locales) for available locales - Defaults to "en_US".

`Timezone` - (Optional) Timezone information of the user. Please look at [Supported Timezone Ids](https://www.opsgenie.com/docs/miscellaneous/supported-timezone-ids) for available timezones - Defaults to "America/New_York".


## Return Values

### Fn::GetAtt

`Id` - The ID of the OpsGenie User.

## See Also

* [opsgenie_user](https://www.terraform.io/docs/providers/opsgenie/r/user.html) in the _Terraform Provider Documentation_
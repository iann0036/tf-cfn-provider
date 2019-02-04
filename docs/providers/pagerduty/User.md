# Terraform::PagerDuty::User

A [user](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users) is a member of a PagerDuty account that have the ability to interact with incidents and other data on the account.

## Properties

`Name` - (Required) The name of the user.

`Email` - (Required) The user's email address.

`Color` - (Optional) The schedule color for the user. Valid options are blue, brown, cayenne, chocolate, crimson, cyan, dark, darkolive, deep, firebrick, forest, goldenrod, gray, green, grey, grey20, indigo, lime, magenta, maroon, medium, midnight, olive, olivedrab, orange, orchid, pink, purple, red, royal, saddle, sea, slate, steel, teal, turquoise or violet.

`Role` - (Optional) The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user`. Can be `admin`, `limited_user`, `owner`, `read_only_user`, `team_responder` or `user`.

`JobTitle` - (Optional) The user's title.

`Teams` - (Optional) A list of teams the user should belong to.

`Description` - (Optional) A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.


## Return Values

### Fn::GetAtt

`Id` - The ID of the user.

`AvatarUrl` - The URL of the user's avatar.

`TimeZone` - The timezone of the user.

`HtmlUrl` - URL at which the entity is uniquely displayed in the Web app.

`InvitationSent` - If true, the user has an outstanding invitation.

## See Also

* [pagerduty_user](https://www.terraform.io/docs/providers/pagerduty/r/user.html) in the _Terraform Provider Documentation_
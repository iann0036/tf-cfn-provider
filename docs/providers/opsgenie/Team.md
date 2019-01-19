# Terraform::OpsGenie::Team

Manages a Team within OpsGenie.

## Properties

`Name` - (Required) The name associated with this team. OpsGenie defines that this must not be longer than 100 characters.

`Description` - (Optional) A description for this team.

`Member` - (Optional) A Member block as documented below.

### Member Properties

`Username` - (Required) The username for the member to add to this Team.

`Role` - (Required) The role for the user within the Team - can be either 'Admin' or 'User'.


## Return Values

### Fn::GetAtt

`Id` - The ID of the OpsGenie User.

## See Also

* [opsgenie_team](https://www.terraform.io/docs/providers/opsgenie/r/team.html) in the _Terraform Provider Documentation_
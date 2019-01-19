# Terraform::Skytap::Project

Provides a Skytap Project resource. Projects are an access permissions model used to share environments, 
templates, and assets with other users.

## Properties

`Name` - (Required) User-defined project name.

`Summary` - (Optional) User-defined description of project.

`AutoAddRoleName` - (Optional) If this field is set to `viewer`, `participant`, `editor`, or `manager`, new users added to your Skytap account are automatically added to this project with the specified project role. Existing users aren’t affected by this setting. If the field is set to `null`, new users aren’t automatically added to the project. For additional details, see [Automatically adding new users to a project](https://help.skytap.com/csh-project-automatic-role.html).

`ShowProjectMembers` - (Optional) Determines whether projects members can view a list of other project members. False by default.


## See Also

* [skytap_project](https://www.terraform.io/docs/providers/skytap/r/project.html) in the _Terraform Provider Documentation_
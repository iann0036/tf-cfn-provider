# Terraform::Google::ProjectIamCustomRole

Allows management of a customized Cloud IAM project role. For more information see
[the official documentation](https://cloud.google.com/iam/docs/understanding-custom-roles)
and
[API](https://cloud.google.com/iam/reference/rest/v1/projects.roles).

~> **Warning:** Note that custom roles in GCP have the concept of a soft-delete. There are two issues that may arise
 from this and how roles are propagated. 1) creating a role may involve undeleting and then updating a role with the
 same name, possibly causing confusing behavior between undelete and update. 2) A deleted role is permanently deleted
 after 7 days, but it can take up to 30 more days (i.e. between 7 and 37 days after deletion) before the role name is
 made available again. This means a deleted role that has been deleted for more than 7 days cannot be changed at all
 by Terraform, and new roles cannot share that name.

## Properties

`RoleId` - (Required) The role id to use for this role.

`Title` - (Required) A human-readable title for the role.

`Project` - (Optional) The project that the service account will be created in. Defaults to the provider project configuration.

`Stage` - (Optional) The current launch stage of the role. Defaults to `GA`. List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

`Description` - (Optional) A human-readable description for the role.


## Return Values

### Fn::GetAtt

`Deleted` - (Optional) The current deleted state of the role.

## See Also

* [google_project_iam_custom_role](https://www.terraform.io/docs/providers/google/r/project_iam_custom_role.html) in the _Terraform Provider Documentation_
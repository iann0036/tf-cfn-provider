# Terraform::Google::Project

Allows creation and management of a Google Cloud Platform project.

Projects created with this resource must be associated with an Organization.
See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

The service account used to run Terraform when creating a `Terraform::Google::Project`
resource must have `roles/resourcemanager.projectCreator`. See the
[Access Control for Organizations Using IAM](https://cloud.google.com/resource-manager/docs/access-control-org)
doc for more information.

Note that prior to 0.8.5, `Terraform::Google::Project` functioned like a data source,
meaning any project referenced by it had to be created and managed outside
Terraform. As of 0.8.5, `Terraform::Google::Project` functions like any other Terraform
resource, with Terraform creating and managing the project. To replicate the old
behavior, either:

* Use the project ID directly in whatever is referencing the project, using the
  [google_project_iam_policy](/docs/providers/google/r/google_project_iam.html)
  to replace the old `policy_data` property.
* Use the [import](/docs/import/usage.html) functionality
  to import your pre-existing project into Terraform, where it can be referenced and
  used just like always, keeping in mind that Terraform will attempt to undo any changes
  made outside Terraform.

~> It's important to note that any project resources that were added to your Terraform config
prior to 0.8.5 will continue to function as they always have, and will not be managed by
Terraform. Only newly added projects are affected.

## Properties

`Name` - (Required) The display name of the project.

`ProjectId` - (Required) The project ID. Changing this forces a new project to be created.

`OrgId` - (Optional) The numeric ID of the organization this project belongs to.
Changing this forces a new project to be created.  Only one of
`OrgId` or `FolderId` may be specified. If the `OrgId` is
specified then the project is created at the top level. Changing
this forces the project to be migrated to the newly specified
organization.

`FolderId` - (Optional) The numeric ID of the folder this project should be
created under. Only one of `OrgId` or `FolderId` may be
specified. If the `FolderId` is specified, then the project is
created under the specified folder. Changing this forces the
project to be migrated to the newly specified folder.

`BillingAccount` - (Optional) The alphanumeric ID of the billing account this project
belongs to. The user or service account performing this operation with Terraform
must have Billing Account Administrator privileges (`roles/billing.admin`) in
the organization. See [Google Cloud Billing API Access Control](https://cloud.google.com/billing/v1/how-tos/access-control)
for more details.

`SkipDelete` - (Optional) If true, the Terraform resource can be deleted
without deleting the Project via the Google API.

`Labels` - (Optional) A set of key/value label pairs to assign to the project.

`AutoCreateNetwork` - (Optional) Create the 'default' network automatically.  Default true.
Note: this might be more accurately described as "Delete Default Network", since the network
is created automatically then deleted before project creation returns, but we choose this
name to match the GCP Console UI. Setting this field to false will enable the Compute Engine
API which is required to delete the network.


## Return Values

### Fn::GetAtt

`Number` - The numeric identifier of the project.

## See Also

* [google_project](https://www.terraform.io/docs/providers/google/r/project.html) in the _Terraform Provider Documentation_
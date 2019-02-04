# Terraform::Tfe::Workspace

Provides a workspace resource.

## Properties

`Name` - (Required) Name of the workspace.

`Organization` - (Required) Name of the organization.

`AutoApply` - (Optional) Whether to automatically apply changes when a
Terraform plan is successful. Defaults to `false`.

`SshKeyId` - (Optional) The ID of an SSH key to assign to the workspace.

`QueueAllRuns` - (Optional) Whether all runs should be queued. When set
to `false`, runs triggered by a VCS change will not be queued until at least
one run is manually queued. Defaults to `true`.

`TerraformVersion` - (Optional) The version of Terraform to use for this
workspace. Defaults to the latest available version.

`WorkingDirectory` - (Optional) A relative path that Terraform will execute
within.  Defaults to the root of your repository.

`VcsRepo` - (Optional) Settings for the workspace's VCS repository.

### VcsRepo Properties

`Identifier` - (Required) A reference to your VCS repository in the format
`:org/:repo` where `:org` and `:repo` refer to the organization and repository
in your VCS provider.

`Branch` - (Optional) The repository branch that Terraform will execute from.
Default to `master`.

`IngressSubmodules` - (Optional) Whether submodules should be fetched when
cloning the VCS repository. Defaults to `false`.

`OauthTokenId` - (Required) Token ID of the VCS Connection (OAuth Conection
+ Token) to use.


## Return Values

### Fn::GetAtt

`Id` - The ID of the workspace within Terraform. This is a custom ID that is.

`ExternalId` - The external ID of the workspace within Terraform Enterprise.

## See Also

* [tfe_workspace](https://www.terraform.io/docs/providers/tfe/r/workspace.html) in the _Terraform Provider Documentation_
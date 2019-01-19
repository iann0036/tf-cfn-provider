# Terraform::AzureRM::SecurityCenterWorkspace

Manages the subscription's Security Center Workspace.

~> **NOTE:** Owner access permission is required.

~> **NOTE:** The subscription's pricing model can not be `Free` for this to have any affect.

## Properties

`Scope` - (Required) The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.

`WorkspaceId` - (Required) The ID of the Log Analytics Workspace to save the data in.


## Return Values

### Fn::GetAtt

`Id` - The Security Center Workspace ID.

## See Also

* [azurerm_security_center_workspace](https://www.terraform.io/docs/providers/azurerm/r/security_center_workspace.html) in the _Terraform Provider Documentation_
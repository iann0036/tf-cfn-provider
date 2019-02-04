# Terraform::AzureAD::Group

Manages a Group within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Read and write all groups` within the `Windows Azure Active Directory` API. In addition it must also have either the `Company Administrator` or `User Account Administrator` Azure Active Directory roles assigned in order to be able to delete groups. You can assign one of the required Azure Active Directory Roles with the **AzureAD PowerShell Module**, which is available for Windows PowerShell or in the Azure Cloud Shell. Please refer to [this documentation](https://docs.microsoft.com/en-us/powershell/module/azuread/add-azureaddirectoryrolemember) for more details.

## Properties

`Name` - (Required) The display name for the Group.


## Return Values

### Fn::GetAtt

`Id` - The Object ID of the Group.

`Name` - The Display Name of the Group.

## See Also

* [azuread_group](https://www.terraform.io/docs/providers/azuread/r/group.html) in the _Terraform Provider Documentation_
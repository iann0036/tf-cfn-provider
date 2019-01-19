# Terraform::AzureRM::ApplicationSecurityGroup

Manage an Application Security Group.

## Properties

`Name` - (Required) Specifies the name of the Application Security Group. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Application Security Group.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Application Security Group.

## See Also

* [azurerm_application_security_group](https://www.terraform.io/docs/providers/azurerm/r/application_security_group.html) in the _Terraform Provider Documentation_
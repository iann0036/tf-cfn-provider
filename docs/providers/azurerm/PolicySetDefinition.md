# Terraform::AzureRM::PolicySetDefinition

Manages a policy set definition. 

-> **NOTE:**  Policy set definitions (also known as policy initiatives) do not take effect until they are assigned to a scope using a Policy Set Assignment.

## Properties

`Name` - (Required) The name of the policy set definition. Changing this forces a new resource to be created.

`PolicyType` - (Required) The policy set type. Possible values are `BuiltIn` or `Custom`. Changing this forces a new resource to be created.

`DisplayName` - (Required) The display name of the policy set definition.

`PolicyDefinitions` - (Required) The policy definitions for the policy set definition. This is a json object representing the bundled policy definitions .

`Description` - (Optional) The description of the policy set definition.

`ManagementGroupId` - (Optional) The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.

`Metadata` - (Optional) The metadata for the policy set definition. This is a json object representing additional metadata that should be stored with the policy definition.

`Parameters` - (Optional) Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.


## Return Values

### Fn::GetAtt

`Id` - The policy set definition id.

## See Also

* [azurerm_policy_set_definition](https://www.terraform.io/docs/providers/azurerm/r/policy_set_definition.html) in the _Terraform Provider Documentation_
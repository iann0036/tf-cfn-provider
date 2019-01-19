# Terraform::AzureRM::PolicyDefinition

Manages a policy rule definition on a management group or your provider subscription. 

Policy definitions do not take effect until they are assigned to a scope using a Policy Assignment.

## Properties

`Name` - (Required) The name of the policy definition. Changing this forces a new resource to be created.

`PolicyType` - (Required) The policy type.  The value can be "BuiltIn", "Custom" or "NotSpecified". Changing this forces a new resource to be created.

`Mode` - (Required) The policy mode that allows you to specify which resource types will be evaluated.  The value can be "All", "Indexed" or "NotSpecified". Changing this resource forces a new resource to be created.

`DisplayName` - (Required) The display name of the policy definition.

`Description` - (Optional) The description of the policy definition.

`ManagementGroupId` - (Optional) The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.

`PolicyRule` - (Optional) The policy rule for the policy definition. This is a json object representing the rule that contains an if and a then block.

`Metadata` - (Optional) The metadata for the policy definition. This is a json object representing additional metadata that should be stored with the policy definition.

`Parameters` - (Optional) Parameters for the policy definition. This field is a json object that allows you to parameterize your policy definition.


## Return Values

### Fn::GetAtt

`Id` - The policy definition id.

## See Also

* [azurerm_policy_definition](https://www.terraform.io/docs/providers/azurerm/r/policy_definition.html) in the _Terraform Provider Documentation_
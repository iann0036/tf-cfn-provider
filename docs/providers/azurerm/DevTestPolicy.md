# Terraform::AzureRM::DevTestPolicy

Manages a Policy within a Dev Test Policy Set.

## Properties

`Name` - (Required) Specifies the name of the Dev Test Policy. Possible values are `GalleryImage`, `LabPremiumVmCount`, `LabTargetCost`, `LabVmCount`, `LabVmSize`, `UserOwnedLabPremiumVmCount`, `UserOwnedLabVmCount` and `UserOwnedLabVmCountInSubnet`. Changing this forces a new resource to be created.

`PolicySetName` - (Required) Specifies the name of the Policy Set within the Dev Test Lab where this policy should be created. Changing this forces a new resource to be created.

`LabName` - (Required) Specifies the name of the Dev Test Lab in which the Policy should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

`Description` - (Optional) A description for the Policy.

`EvaluatorType` - (Required) The Evaluation Type used for this Policy. Possible values include: 'AllowedValuesPolicy', 'MaxValuePolicy'. Changing this forces a new resource to be created.

`Threshold` - (Required) The Threshold for this Policy.

`FactData` - (Optional) The Fact Data for this Policy.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Dev Test Policy.

## See Also

* [azurerm_dev_test_policy](https://www.terraform.io/docs/providers/azurerm/r/dev_test_policy.html) in the _Terraform Provider Documentation_
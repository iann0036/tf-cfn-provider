# Terraform::AzureRM::DevTestLab

Manages a Dev Test Lab.

## Properties

`Name` - (Required) Specifies the name of the Dev Test Lab. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group under which the Dev Test Lab resource has to be created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the Dev Test Lab should exist. Changing this forces a new resource to be created.

`StorageType` - (Optional) The type of storage used by the Dev Test Lab. Possible values are `Standard` and `Premium`. Defaults to `Premium`. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Dev Test Lab.

`ArtifactsStorageAccountId` - The ID of the Storage Account used for Artifact Storage.

`DefaultStorageAccountId` - The ID of the Default Storage Account for this Dev Test Lab.

`DefaultPremiumStorageAccountId` - The ID of the Default Premium Storage Account for this Dev Test Lab.

`KeyVaultId` - The ID of the Key used for this Dev Test Lab.

`PremiumDataDiskStorageAccountId` - The ID of the Storage Account used for Storage of Premium Data Disk.

`UniqueIdentifier` - The unique immutable identifier of the Dev Test Lab.

## See Also

* [azurerm_dev_test_lab](https://www.terraform.io/docs/providers/azurerm/r/dev_test_lab.html) in the _Terraform Provider Documentation_
# Terraform::AzureRM::BatchAccount

Manages an Azure Batch account.

## Properties

`Name` - (Required) Specifies the name of the Batch account. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`PoolAllocationMode` - (Optional) Specifies the mode to use for pool allocation. Possible values are `BatchService` or `UserSubscription`. Defaults to `BatchService`.

`StorageAccountId` - (Optional) Specifies the storage account to use for the Batch account. If not specified, Azure Batch will manage the storage.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Batch account ID.

## See Also

* [azurerm_batch_account](https://www.terraform.io/docs/providers/azurerm/r/batch_account.html) in the _Terraform Provider Documentation_
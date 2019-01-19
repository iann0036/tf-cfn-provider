# Terraform::AzureRM::BatchPool

Manages an Azure Batch pool.

## Properties

`Name` - (Required) Specifies the name of the Batch pool. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.

`AccountName` - (Required) Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.

`NodeAgentSkuId` - (Required) Specifies the Sku of the node agents that will be created in the Batch pool.

`VmSize` - (Required) Specifies the size of the VM created in the Batch pool.

`StorageImageReference` - (Required) A `StorageImageReference` for the virtual machines that will compose the Batch pool.

`DisplayName` - (Optional) Specifies the display name of the Batch pool.

`FixedScale` - (Optional) A `FixedScale` block that describes the scale settings when using fixed scale.

`AutoScale` - (Optional) A `AutoScale` block that describes the scale settings when using auto scale.

`StartTask` - (Optional) A `StartTask` block that describes the start task settings for the Batch pool.

### FixedScale Properties

`TargetDedicatedNodes` - (Optional) The number of nodes in the Batch pool. Defaults to `1`.

`TargetLowPriorityNodes` - (Optional) The number of low priority nodes in the Batch pool. Defaults to `0`.

`ResizeTimeout` - (Optional) The timeout for resize operations. Defaults to `PT15M`.

### AutoScale Properties

`EvaluationInterval` - (Optional) The interval to wait before evaluating if the pool needs to be scaled. Defaults to `PT15M`.

`Formula` - (Required) The autoscale formula that needs to be used for scaling the Batch pool.

### StartTask Properties

`CommandLine` - (Required) The command line executed by the start task.

`MaxTaskRetryCount` - (Optional) The number of retry count. Defaults to `1`.

`WaitForSuccess` - (Optional) A flag that indicates if the Batch pool should wait for the start task to be completed. Default to `false`.

`Environment` - (Optional) A map of strings (key,value) that represents the environment variables to set in the start task.

`UserIdentity` - (Required) A `UserIdentity` block that describes the user identity under which the start task runs.

### UserIdentity Properties

`UserName` - (Optional) The username to be used by the Batch pool start task.

`AutoUser` - (Optional) A `AutoUser` block that describes the user identity under which the start task runs.

### AutoUser Properties

`ElevationLevel` - (Optional) The elevation level of the user identity under which the start task runs. Possible values are `Admin` or `NonAdmin`. Defaults to `NonAdmin`.

`Scope` - (Optional) The scope of the user identity under which the start task runs. Possible values are `Task` or `Pool`. Defaults to `Task`.


## Return Values

### Fn::GetAtt

`Id` - The Batch pool ID.

## See Also

* [azurerm_batch_pool](https://www.terraform.io/docs/providers/azurerm/r/batch_pool.html) in the _Terraform Provider Documentation_
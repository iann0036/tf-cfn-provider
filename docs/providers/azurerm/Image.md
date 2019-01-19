# Terraform::AzureRM::Image

Manage a custom virtual machine image that can be used to create virtual machines.

## Properties

`Name` - (Required) Specifies the name of the image. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the image. Changing this forces a new resource to be created.

`Location` - (Required) Specified the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`SourceVirtualMachineId` - (Optional) The Virtual Machine ID from which to create the image.

`OsDisk` - (Optional) One or more `OsDisk` elements as defined below.

`DataDisk` - (Optional) One or more `DataDisk` elements as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### OsDisk Properties

`OsType` - (Required) Specifies the type of operating system contained in the the virtual machine image. Possible values are: Windows or Linux.

`OsState` - (Required) Specifies the state of the operating system contained in the blob. Currently, the only value is Generalized.

`ManagedDiskId` - (Optional) Specifies the ID of the managed disk resource that you want to use to create the image.

`BlobUri` - (Optional) Specifies the URI in Azure storage of the blob that you want to use to create the image.

`Caching` - (Optional) Specifies the caching mode as `ReadWrite`, `ReadOnly`, or `None`. The default is `None`.

`SizeGb` - (Optional) Specifies the size of the image to be created. The target size can't be smaller than the source size.

### DataDisk Properties

`Lun` - (Required) Specifies the logical unit number of the data disk.

`ManagedDiskId` - (Optional) Specifies the ID of the managed disk resource that you want to use to create the image.

`BlobUri` - (Optional) Specifies the URI in Azure storage of the blob that you want to use to create the image.

`Caching` - (Optional) Specifies the caching mode as `ReadWrite`, `ReadOnly`, or `None`. The default is `None`.

`SizeGb` - (Optional) Specifies the size of the image to be created. The target size can't be smaller than the source size.


## Return Values

### Fn::GetAtt

`Id` - The managed image ID.

## See Also

* [azurerm_image](https://www.terraform.io/docs/providers/azurerm/r/image.html) in the _Terraform Provider Documentation_
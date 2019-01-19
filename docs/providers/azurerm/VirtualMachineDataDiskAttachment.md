# Terraform::AzureRM::VirtualMachineDataDiskAttachment

Manages attaching a Disk to a Virtual Machine.

~> **NOTE:** Data Disks can be attached either directly on the `Terraform::AzureRM::VirtualMachine` resource, or using the `azurermVirtualMachineDataDiskAttachment` resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.

-> **Please Note:** only Managed Disks are supported via this separate resource, Unmanaged Disks can be attached using the `storage_data_disk` block in the `Terraform::AzureRM::VirtualMachine` resource.

## Properties

`VirtualMachineId` - (Required) The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.

`ManagedDiskId` - (Required) The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.

`Lun` - (Required) The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.

`Caching` - (Required) Specifies the caching requirements for this Data Disk. Possible values include `None`, `ReadOnly` and `ReadWrite`.

`CreateOption` - (Optional) The Create Option of the Data Disk, such as `Empty` or `Attach`. Defaults to `Attach`. Changing this forces a new resource to be created.

`WriteAcceleratorEnabled` - (Optional) Specifies if Write Accelerator is enabled on the disk. This can only be enabled on `Premium_LRS` managed disks with no caching and [M-Series VMs](https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator). Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Virtual Machine Data Disk attachment.

## See Also

* [azurerm_virtual_machine_data_disk_attachment](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_data_disk_attachment.html) in the _Terraform Provider Documentation_
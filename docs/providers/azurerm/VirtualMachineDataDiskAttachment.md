# Terraform::AzureRM::VirtualMachineDataDiskAttachment

Manages attaching a Disk to a Virtual Machine.

~> **NOTE:** Data Disks can be attached either directly on the `azurerm_virtual_machine` resource, or using the `azurerm_virtual_machine_data_disk_attachment` resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.

-> **Please Note:** only Managed Disks are supported via this separate resource, Unmanaged Disks can be attached using the `storage_data_disk` block in the `azurerm_virtual_machine` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the Virtual Machine Data Disk attachment.

## See Also

* [azurerm_virtual_machine_data_disk_attachment](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_data_disk_attachment.html) in the _Terraform Provider Documentation_
# Terraform::AzureRM::VirtualMachine

Manages a Virtual Machine.

~> **NOTE:** Data Disks can be attached either directly on the `azurerm_virtual_machine` resource, or using the `azurerm_virtual_machine_data_disk_attachment` resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the Virtual Machine.

## See Also

* [azurerm_virtual_machine](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine.html) in the _Terraform Provider Documentation_
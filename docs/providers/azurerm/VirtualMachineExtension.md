# Terraform::AzureRM::VirtualMachineExtension

Manages a Virtual Machine Extension to provide post deployment configuration
and run automated tasks.

~> **NOTE:** Custom Script Extensions for Linux & Windows require that the `commandToExecute` returns a `0` exit code to be classified as successfully deployed. You can achieve this by appending `exit 0` to the end of your `commandToExecute`.

-> **NOTE:** Custom Script Extensions require that the Azure Virtual Machine Guest Agent is running on the Virtual Machine.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Virtual Machine Extension ID.

## See Also

* [azurerm_virtual_machine_extension](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_extension.html) in the _Terraform Provider Documentation_
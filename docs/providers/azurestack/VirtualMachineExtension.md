# Terraform::AzureStack::VirtualMachineExtension

Creates a new Virtual Machine Extension to provide post deployment configuration
and run automated tasks.

~> **Please Note:** The CustomScript extensions for Linux & Windows require that the `commandToExecute` returns a `0` exit code to be classified as successfully deployed. You can achieve this by appending `exit 0` to the end of your `commandToExecute`.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Virtual Machine Extension ID.

## See Also

* [azurestack_virtual_machine_extension](https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension.html) in the _Terraform Provider Documentation_
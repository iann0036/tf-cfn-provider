# Terraform::AzureStack::VirtualMachineExtension

Creates a new Virtual Machine Extension to provide post deployment configuration
and run automated tasks.

~> **Please Note:** The CustomScript extensions for Linux & Windows require that the `commandToExecute` returns a `0` exit code to be classified as successfully deployed. You can achieve this by appending `exit 0` to the end of your `commandToExecute`.

## Properties

`Name` - (Required) The name of the virtual machine extension peering. Changing this forces a new resource to be created.

`Location` - (Required) The location where the extension is created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the virtual network. Changing this forces a new resource to be created.

`VirtualMachineName` - (Required) The name of the virtual machine. Changing this forces a new resource to be created.

`Publisher` - (Required) The publisher of the extension, available publishers can be found by using the Azure CLI.

`Type` - (Required) The type of extension, available types for a publisher can be found using the Azure CLI.

`TypeHandlerVersion` - (Required) Specifies the version of the extension to use, available versions can be found using the Azure CLI.

`AutoUpgradeMinorVersion` - (Optional) Specifies if the platform deploys the latest minor version update to the `TypeHandlerVersion` specified.

`Settings` - (Required) The settings passed to the extension, these are specified as a JSON object in a string.

`ProtectedSettings` - (Optional) The protected_settings passed to the extension, like settings, these are specified as a JSON object in a string.


## Return Values

### Fn::GetAtt

`Id` - The Virtual Machine Extension ID.

## See Also

* [azurestack_virtual_machine_extension](https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension.html) in the _Terraform Provider Documentation_
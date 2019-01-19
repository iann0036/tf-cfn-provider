# Terraform::AzureStack::VirtualMachineScaleSet

Manages a virtual machine scale set.

~> **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The virtual machine scale set ID.

`BootDiagnostics` - A boot diagnostics profile block as referenced below.

## See Also

* [azurestack_virtual_machine_scale_set](https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set.html) in the _Terraform Provider Documentation_
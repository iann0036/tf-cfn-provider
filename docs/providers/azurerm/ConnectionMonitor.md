# Terraform::AzureRM::ConnectionMonitor

Configures a Connection Monitor to monitor communication between a Virtual Machine and an endpoint using a Network Watcher.

## Properties

`Name` - (Required) The name of the Connection Monitor. Changing this forces a new resource to be created.

`NetworkWatcherName` - (Required) The name of the Network Watcher. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Connection Monitor. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`AutoStart` - (Optional) Specifies whether the connection monitor will start automatically once created. Defaults to `true`. Changing this forces a new resource to be created.

`IntervalInSeconds` - (Optional) Monitoring interval in seconds. Defaults to `60`.

`Source` - (Required) A `Source` block as defined below.

`Destination` - (Required) A `Destination` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Source Properties

`VirtualMachineId` - (Required) The ID of the Virtual Machine to monitor connectivity from.

`Port` - (Optional) The port on the Virtual Machine to monitor connectivity from. Defaults to `0` (Dynamic Port Assignment).

### Destination Properties

`VirtualMachineId` - (Optional) The ID of the Virtual Machine to monitor connectivity to.

`Address` - (Optional) IP address or domain name to monitor connectivity to.

`Port` - (Required) The port on the destination to monitor connectivity to.


## Return Values

### Fn::GetAtt

`Id` - The Connection Monitor ID.

## See Also

* [azurerm_connection_monitor](https://www.terraform.io/docs/providers/azurerm/r/connection_monitor.html) in the _Terraform Provider Documentation_
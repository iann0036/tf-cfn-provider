# Terraform::AzureRM::PacketCapture

Configures Packet Capturing against a Virtual Machine using a Network Watcher.

## Properties

`Name` - (Required) The name to use for this Packet Capture. Changing this forces a new resource to be created.

`NetworkWatcherName` - (Required) The name of the Network Watcher. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.

`TargetResourceId` - (Required) The ID of the Resource to capture packets from. Changing this forces a new resource to be created.

`MaximumBytesPerPacket` - (Optional) The number of bytes captured per packet. The remaining bytes are truncated. Defaults to `0` (Entire Packet Captured). Changing this forces a new resource to be created.

`MaximumBytesPerSession` - (Optional) Maximum size of the capture in Bytes. Defaults to `1073741824` (1GB). Changing this forces a new resource to be created.

`MaximumCaptureDuration` - (Optional) The maximum duration of the capture session in seconds. Defaults to `18000` (5 hours). Changing this forces a new resource to be created.

`StorageLocation` - (Required) A `StorageLocation` block as defined below. Changing this forces a new resource to be created.

`Filter` - (Optional) One or more `Filter` blocks as defined below. Changing this forces a new resource to be created.

### StorageLocation Properties

`FilePath` - (Optional) A valid local path on the targeting VM. Must include the name of the capture file (*.cap). For linux virtual machine it must start with `/var/captures`.

`StorageAccountId` - (Optional) The ID of the storage account to save the packet capture session.

### Filter Properties

`LocalIpAddress` - (Optional) The local IP Address to be filtered on. Notation: "127.0.0.1" for single address entry. "127.0.0.1-127.0.0.255" for range. "127.0.0.1;127.0.0.5" for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Changing this forces a new resource to be created.

`LocalPort` - (Optional) The local port to be filtered on. Notation: "80" for single port entry."80-85" for range. "80;443;" for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Changing this forces a new resource to be created.

`Protocol` - (Required) The Protocol to be filtered on. Possible values include `Any`, `TCP` and `UDP`. Changing this forces a new resource to be created.

`RemoteIpAddress` - (Optional) The remote IP Address to be filtered on. Notation: "127.0.0.1" for single address entry. "127.0.0.1-127.0.0.255" for range. "127.0.0.1;127.0.0.5;" for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported.. Changing this forces a new resource to be created.

`RemotePort` - (Optional) The remote port to be filtered on. Notation: "80" for single port entry."80-85" for range. "80;443;" for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The Packet Capture ID.

`StorageLocation` - (Required) A `StorageLocation` block as defined below.

`StoragePath` - The URI of the storage path to save the packet capture.

## See Also

* [azurerm_packet_capture](https://www.terraform.io/docs/providers/azurerm/r/packet_capture.html) in the _Terraform Provider Documentation_
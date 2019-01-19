# Terraform::AzureRM::Eventhub

Manages a Event Hubs as a nested resource within a Event Hubs namespace.

## Properties

`NamespaceName` - (Required) Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.

`PartitionCount` - (Required) Specifies the current number of shards on the Event Hub. Changing this forces a new resource to be created.

`MessageRetention` - (Required) Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.

`CaptureDescription` - (Optional) A `CaptureDescription` block as defined below.

### Destination Properties

`Name` - (Required) The Name of the Destination where the capture should take place. At this time the only supported value is `EventHubArchive.AzureBlockBlob`.

`ArchiveNameFormat` - The Blob naming convention for archiving. e.g. `{Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}`. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order.

`BlobContainerName` - (Required) The name of the Container within the Blob Storage Account where messages should be archived.

`StorageAccountId` - (Required) The ID of the Blob Storage Account where messages should be archived.

### CaptureDescription Properties

`Enabled` - (Required) Specifies if the Capture Description is Enabled.

`Encoding` - (Required) Specifies the Encoding used for the Capture Description. Possible values are `Avro` and `AvroDeflate`.

`IntervalInSeconds` - (Optional) Specifies the time interval in seconds at which the capture will happen. Values can be between `60` and `900` seconds. Defaults to `300` seconds.

`SizeLimitInBytes` - (Optional) Specifies the amount of data built up in your EventHub before a Capture Operation occurs. Value should be between `10485760` and `524288000`  bytes. Defaults to `314572800` bytes.

`Destination` - (Required) A `Destination` block as defined below.


## Return Values

### Fn::GetAtt

`Id` - The EventHub ID.

`PartitionIds` - The identifiers for partitions created for Event Hubs.

## See Also

* [azurerm_eventhub](https://www.terraform.io/docs/providers/azurerm/r/eventhub.html) in the _Terraform Provider Documentation_
# Terraform::AzureRM::ServicebusTopic

Manage a ServiceBus Topic.

**Note** Topics can only be created in Namespaces with an SKU of `standard` or higher.

## Properties

`Name` - (Required) Specifies the name of the ServiceBus Topic resource. Changing this forces a new resource to be created.

`NamespaceName` - (Required) The name of the ServiceBus Namespace to create this topic in. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

`Status` - (Optional) The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

`AutoDeleteOnIdle` - (Optional) The ISO 8601 timespan duration of the idle interval after which the Topic is automatically deleted, minimum of 5 minutes.

`DefaultMessageTtl` - (Optional) The ISO 8601 timespan duration of TTL of messages sent to this topic if no TTL value is set on the message itself.

`DuplicateDetectionHistoryTimeWindow` - (Optional) The ISO 8601 timespan duration during which duplicates can be detected. Defaults to 10 minutes. (`PT10M`).

`EnableBatchedOperations` - (Optional) Boolean flag which controls if server-side batched operations are enabled. Defaults to false.

`EnableExpress` - (Optional) Boolean flag which controls whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage. Defaults to false.

`EnablePartitioning` - (Optional) Boolean flag which controls whether to enable the topic to be partitioned across multiple message brokers. Defaults to false. Changing this forces a new resource to be created.

`MaxSizeInMegabytes` - (Optional) Integer value which controls the size of memory allocated for the topic. For supported values see the "Queue/topic size" section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

`RequiresDuplicateDetection` - (Optional) Boolean flag which controls whether the Topic requires duplicate detection. Defaults to false. Changing this forces a new resource to be created.

`SupportOrdering` - (Optional) Boolean flag which controls whether the Topic supports ordering. Defaults to false.


## Return Values

### Fn::GetAtt

`Id` - The ServiceBus Topic ID.

## See Also

* [azurerm_servicebus_topic](https://www.terraform.io/docs/providers/azurerm/r/servicebus_topic.html) in the _Terraform Provider Documentation_
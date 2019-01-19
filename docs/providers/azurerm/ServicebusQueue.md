# Terraform::AzureRM::ServicebusQueue

Manage and manage a ServiceBus Queue.

## Properties

`Name` - (Required) Specifies the name of the ServiceBus Queue resource. Changing this forces a new resource to be created.

`NamespaceName` - (Required) The name of the ServiceBus Namespace to create this queue in. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

`AutoDeleteOnIdle` - (Optional) The ISO 8601 timespan duration of the idle interval after which the Queue is automatically deleted, minimum of 5 minutes.

`DefaultMessageTtl` - (Optional) The ISO 8601 timespan duration of the TTL of messages sent to this queue. This is the default value used when TTL is not set on message itself.

`DuplicateDetectionHistoryTimeWindow` - (Optional) The ISO 8601 timespan duration during which duplicates can be detected. Default value is 10 minutes. (`PT10M`).

`EnableExpress` - (Optional) Boolean flag which controls whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST be set to `false`.

`EnablePartitioning` - (Optional) Boolean flag which controls whether to enable the queue to be partitioned across multiple message brokers. Changing this forces a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST be set to `true`.

`LockDuration` - (Optional) The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`).

`MaxSizeInMegabytes` - (Optional) Integer value which controls the size of memory allocated for the queue. For supported values see the "Queue/topic size" section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

`RequiresDuplicateDetection` - (Optional) Boolean flag which controls whether the Queue requires duplicate detection. Changing this forces a new resource to be created. Defaults to `false`.

`RequiresSession` - (Optional) Boolean flag which controls whether the Queue requires sessions. This will allow ordered handling of unbounded sequences of related messages. With sessions enabled a queue can guarantee first-in-first-out delivery of messages. Changing this forces a new resource to be created. Defaults to `false`.

`DeadLetteringOnMessageExpiration` - (Optional) Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

`MaxDeliveryCount` - (Optional) Integer value which controls when a message is automatically deadlettered. Defaults to `10`.


## Return Values

### Fn::GetAtt

`Id` - The ServiceBus Queue ID.

## See Also

* [azurerm_servicebus_queue](https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue.html) in the _Terraform Provider Documentation_
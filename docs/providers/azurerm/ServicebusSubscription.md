# Terraform::AzureRM::ServicebusSubscription

Manage a ServiceBus Subscription.

## Properties

`Name` - (Required) Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.

`NamespaceName` - (Required) The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.

`TopicName` - (Required) The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

`MaxDeliveryCount` - (Required) The maximum number of deliveries.

`AutoDeleteOnIdle` - (Optional) The idle interval after which the Subscription is automatically deleted, minimum of 5 minutes. Provided in the [TimeSpan](#timespan-format) format.

`DefaultMessageTtl` - (Optional) The TTL of messages sent to this Subscription if no TTL value is set on the message itself. Provided in the [TimeSpan](#timespan-format) format.

`LockDuration` - (Optional) The lock duration for the subscription, maximum supported value is 5 minutes. Defaults to 1 minute.

`DeadLetteringOnMessageExpiration` - (Optional) Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to false.

`EnableBatchedOperations` - (Optional) Boolean flag which controls whether the Subscription supports batched operations. Defaults to false.

`RequiresSession` - (Optional) Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to false. Changing this forces a new resource to be created.

`ForwardTo` - (Optional) The name of a Queue or Topic to automatically forward messages to.


## Return Values

### Fn::GetAtt

`Id` - The ServiceBus Subscription ID.

## See Also

* [azurerm_servicebus_subscription](https://www.terraform.io/docs/providers/azurerm/r/servicebus_subscription.html) in the _Terraform Provider Documentation_
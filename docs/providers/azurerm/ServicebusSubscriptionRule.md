# Terraform::AzureRM::ServicebusSubscriptionRule

Manage a ServiceBus Subscription Rule.

## Properties

`Name` - (Required) Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.

`NamespaceName` - (Required) The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.

`TopicName` - (Required) The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.

`SubscriptionName` - (Required) The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.

`FilterType` - (Required) Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.

`SqlFilter` - (Optional) Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `FilterType` is set to `SqlFilter`.

`CorrelationFilter` - (Optional) A `CorrelationFilter` block as documented below to be evaluated against a BrokeredMessage. Required when `FilterType` is set to `CorrelationFilter`.

`Action` - (Optional) Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.

### CorrelationFilter Properties

`ContentType` - (Optional) Content type of the message.

`CorrelationId` - (Optional) Identifier of the correlation.

`Label` - (Optional) Application specific label.

`MessageId` - (Optional) Identifier of the message.

`ReplyTo` - (Optional) Address of the queue to reply to.

`ReplyToSessionId` - (Optional) Session identifier to reply to.

`SessionId` - (Optional) Session identifier.

`To` - (Optional) Address to send to.


## Return Values

### Fn::GetAtt

`Id` - The ServiceBus Subscription Rule ID.

## See Also

* [azurerm_servicebus_subscription_rule](https://www.terraform.io/docs/providers/azurerm/r/servicebus_subscription_rule.html) in the _Terraform Provider Documentation_
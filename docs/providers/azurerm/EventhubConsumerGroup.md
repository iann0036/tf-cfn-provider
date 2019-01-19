# Terraform::AzureRM::EventhubConsumerGroup

Manages a Event Hubs Consumer Group as a nested resource within an Event Hub.

## Properties

`Name` - (Required) Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.

`NamespaceName` - (Required) Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

`EventhubName` - (Required) Specifies the name of the EventHub. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists. Changing this forces a new resource to be created.

`UserMetadata` - (Optional) Specifies the user metadata.


## Return Values

### Fn::GetAtt

`Id` - The EventHub Consumer Group ID.

## See Also

* [azurerm_eventhub_consumer_group](https://www.terraform.io/docs/providers/azurerm/r/eventhub_consumer_group.html) in the _Terraform Provider Documentation_
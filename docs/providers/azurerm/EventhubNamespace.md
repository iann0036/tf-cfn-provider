# Terraform::AzureRM::EventhubNamespace

Manage an EventHub Namespace.

## Properties

`Name` - (Required) Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) Defines which tier to use. Valid options are `Basic` and `Standard`.

`Capacity` - (Optional) Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.

`AutoInflateEnabled` - (Optional) Is Auto Inflate enabled for the EventHub Namespace?.

`MaximumThroughputUnits` - (Optional) Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.

`KafkaEnabled` - (Optional) Is Kafka enabled for the EventHub Namespace? Defaults to `false`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The EventHub Namespace ID.

`DefaultPrimaryConnectionString` - The primary connection string for the authorization.

`DefaultSecondaryConnectionString` - The secondary connection string for the.

`DefaultPrimaryKey` - The primary access key for the authorization rule `RootManageSharedAccessKey`.

`DefaultSecondaryKey` - The secondary access key for the authorization rule `RootManageSharedAccessKey`.

## See Also

* [azurerm_eventhub_namespace](https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace.html) in the _Terraform Provider Documentation_
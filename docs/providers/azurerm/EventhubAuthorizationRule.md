# Terraform::AzureRM::EventhubAuthorizationRule

Manages a Event Hubs authorization Rule within an Event Hub.

## Properties

`Name` - (Required) Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.

`NamespaceName` - (Required) Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

`EventhubName` - (Required) Specifies the name of the EventHub. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

`Listen` - (Optional) Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.

`Send` - (Optional) Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.

`Manage` - (Optional) Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `Listen` and `Send` must be too. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The EventHub ID.

`PrimaryKey` - The Primary Key for the Event Hubs authorization Rule.

`PrimaryConnectionString` - The Primary Connection String for the Event Hubs authorization Rule.

`SecondaryKey` - The Secondary Key for the Event Hubs authorization Rule.

`SecondaryConnectionString` - The Secondary Connection String for the Event Hubs authorization Rule.

## See Also

* [azurerm_eventhub_authorization_rule](https://www.terraform.io/docs/providers/azurerm/r/eventhub_authorization_rule.html) in the _Terraform Provider Documentation_
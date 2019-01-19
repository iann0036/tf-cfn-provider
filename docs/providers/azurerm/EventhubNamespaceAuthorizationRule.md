# Terraform::AzureRM::EventhubNamespaceAuthorizationRule

Manages an Authorization Rule for an Event Hub Namespace.

## Properties

`Name` - (Required) Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

`NamespaceName` - (Required) Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

`Listen` - (Optional) Grants listen access to this this Authorization Rule. Defaults to `false`.

`Send` - (Optional) Grants send access to this this Authorization Rule. Defaults to `false`.

`Manage` - (Optional) Grants manage access to this this Authorization Rule. When this property is `true` - both `Listen` and `Send` must be too. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The EventHub ID.

`PrimaryKey` - The Primary Key for the Authorization Rule.

`PrimaryConnectionString` - The Primary Connection String for the Authorization Rule.

`SecondaryKey` - The Secondary Key for the Authorization Rule.

`SecondaryConnectionString` - The Secondary Connection String for the Authorization Rule.

## See Also

* [azurerm_eventhub_namespace_authorization_rule](https://www.terraform.io/docs/providers/azurerm/r/eventhub_namespace_authorization_rule.html) in the _Terraform Provider Documentation_
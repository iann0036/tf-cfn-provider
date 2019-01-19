# Terraform::AzureRM::NotificationHubAuthorizationRule

Manages an Authorization Rule associated with a Notification Hub within a Notification Hub Namespace.

## Properties

`Name` - (Required) The name to use for this Authorization Rule. Changing this forces a new resource to be created.

`NotificationHubName` - (Required) The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.

`NamespaceName` - (Required) The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

`Manage` - (Optional) Does this Authorization Rule have Manage access to the Notification Hub? Defaults to `false`.

`Send` - (Optional) Does this Authorization Rule have Send access to the Notification Hub? Defaults to `false`.

`Listen` - (Optional) Does this Authorization Rule have Listen access to the Notification Hub? Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Authorization Rule.

`PrimaryAccessKey` - The Primary Access Key associated with this Authorization Rule.

`SecondaryAccessKey` - The Secondary Access Key associated with this Authorization Rule.

## See Also

* [azurerm_notification_hub_authorization_rule](https://www.terraform.io/docs/providers/azurerm/r/notification_hub_authorization_rule.html) in the _Terraform Provider Documentation_
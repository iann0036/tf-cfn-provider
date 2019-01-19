# Terraform::AzureRM::NotificationHubNamespace

Manages a Notification Hub Namespace.

## Properties

`ResourceGroupName` - (Required) The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.

`Location` - (Required) The Azure Region in which this Notification Hub Namespace should be created.

`NamespaceType` - (Required) The Type of Namespace - possible values are `Messaging` or `NotificationHub`. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as defined below.

`Enabled` - (Optional) Is this Notification Hub Namespace enabled? Defaults to `true`.

### Sku Properties

`Name` - (Required) The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard`. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Notification Hub Namespace.

`ServicebusEndpoint` - The ServiceBus Endpoint for this Notification Hub Namespace.

## See Also

* [azurerm_notification_hub_namespace](https://www.terraform.io/docs/providers/azurerm/r/notification_hub_namespace.html) in the _Terraform Provider Documentation_
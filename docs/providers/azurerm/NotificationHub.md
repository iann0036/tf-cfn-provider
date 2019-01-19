# Terraform::AzureRM::NotificationHub

Manages a Notification Hub within a Notification Hub Namespace.

## Properties

`Name` - (Required) The name to use for this Notification Hub. Changing this forces a new resource to be created.

`NamespaceName` - (Required) The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

`Location` - (Required) The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.

`ApnsCredential` - (Optional) A `ApnsCredential` block as defined below.

`GcmCredential` - (Optional) A `GcmCredential` block as defined below.

### ApnsCredential Properties

`ApplicationMode` - (Required) The Application Mode which defines which server the APNS Messages should be sent to. Possible values are `Production` and `Sandbox`.

`BundleId` - (Required) The Bundle ID of the iOS/macOS application to send push notifications for, such as `com.hashicorp.example`.

`KeyId` - (Required) The Apple Push Notifications Service (APNS) Key.

`TeamId` - (Required) The ID of the team the Token.

`Token` - (Required) The Push Token associated with the Apple Developer Account. This is the contents of the `key` downloaded from [the Apple Developer Portal](https://developer.apple.com/account/ios/authkey/) between the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` blocks.

### GcmCredential Properties

`ApiKey` - (Required) The API Key associated with the Google Cloud Messaging service.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Notification Hub.

## See Also

* [azurerm_notification_hub](https://www.terraform.io/docs/providers/azurerm/r/notification_hub.html) in the _Terraform Provider Documentation_
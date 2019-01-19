# Terraform::AzureRM::SecurityCenterContact

Manages the subscription's Security Center Contact.

~> **NOTE:** Owner access permission is required.

## Properties

`Email` - (Required) The email of the Security Center Contact.

`Phone` - (Required) The phone number of the Security Center Contact.

`AlertNotifications` - (Required) Whether to send security alerts notifications to the security contact.

`AlertsToAdmins` - (Required) Whether to send security alerts notifications to subscription admins.


## Return Values

### Fn::GetAtt

`Id` - The Security Center Contact ID.

## See Also

* [azurerm_security_center_contact](https://www.terraform.io/docs/providers/azurerm/r/security_center_contact.html) in the _Terraform Provider Documentation_
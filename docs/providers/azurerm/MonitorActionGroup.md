# Terraform::AzureRM::MonitorActionGroup

Manages an Action Group within Azure Monitor.

## Properties

`Name` - (Required) The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Action Group instance.

`ShortName` - (Required) The short name of the action group. This will be used in SMS messages.

`Enabled` - (Optional) Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to `true`.

`EmailReceiver` - (Optional) One or more `EmailReceiver` blocks as defined below.

`SmsReceiver` - (Optional) One or more `sms_receiver ` blocks as defined below.

`WebhookReceiver` - (Optional) One or more `webhook_receiver ` blocks as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`EmailAddress` - (Required) The email address of this receiver.

`CountryCode` - (Required) The country code of the SMS receiver.

`PhoneNumber` - (Required) The phone number of the SMS receiver.

`ServiceUri` - (Required) The URI where webhooks should be sent.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Action Group.

## See Also

* [azurerm_monitor_action_group](https://www.terraform.io/docs/providers/azurerm/r/monitor_action_group.html) in the _Terraform Provider Documentation_
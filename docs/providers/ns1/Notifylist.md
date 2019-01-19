# Terraform::NS1::Notifylist

Provides a NS1 Notify List resource. This can be used to create, modify, and delete notify lists.

## Properties

`Name` - (Required) The free-form display name for the notify list.

`Notifications` - (Optional) A list of notifiers. All notifiers in a notification list will receive notifications whenever an event is send to the list (e.g., when a monitoring job fails). Notifiers are documented below.

### Notifications Properties

`Type` - (Required) The type of notifier. Available notifiers are indicated in /notifytypes endpoint.

`Config` - (Required) Configuration details for the given notifier type.


## See Also

* [ns1_notifylist](https://www.terraform.io/docs/providers/ns1/r/notifylist.html) in the _Terraform Provider Documentation_
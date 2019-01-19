# Terraform::Icinga2::Notification

Configures an Icinga2 notification resource. This allows notifications to be configured, updated,
and deleted.

## Properties

`Hostname` - (Required) The hostname the notification applies to.

`Command` - (Required) Notification command to use.

`Users` - (Required) List of users to notification.

`Servicename` - (Optional) Service to send notification for.


## See Also

* [icinga2_notification](https://www.terraform.io/docs/providers/icinga2/r/notification.html) in the _Terraform Provider Documentation_
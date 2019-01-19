# Terraform::NS1::User

Provides a NS1 User resource. Creating a user sends an invitation email to the user's email address. This can be used to create, modify, and delete users.

## Properties

`Name` - (Required) The free form name of the user.

`Username` - (Required) The users login name.

`Email` - (Required) The email address of the user.

`Notify` - (Required) The Whether or not to notify the user of specified events. Only `billing` is available currently.

`Teams` - (Required) The teams that the user belongs to.

`Permissions` - (Optional) The allowed permissions of the user. Permissions documented below.

`DnsViewZones` - (Optional) Whether the user can view the accounts zones.

`DnsManageZones` - (Optional) Whether the user can modify the accounts zones.

`DnsZonesAllowByDefault` - (Optional) If true, enable the `DnsZonesAllow` list, otherwise enable the `DnsZonesDeny` list.

`DnsZonesAllow` - (Optional) List of zones that the user may access.

`DnsZonesDeny` - (Optional) List of zones that the user may not access.

`DataPushToDatafeeds` - (Optional) Whether the user can publish to data feeds.

`DataManageDatasources` - (Optional) Whether the user can modify data sources.

`DataManageDatafeeds` - (Optional) Whether the user can modify data feeds.

`AccountManageUsers` - (Optional) Whether the user can modify account users.

`AccountManagePaymentMethods` - (Optional) Whether the user can modify account payment methods.

`AccountManagePlan` - (Optional) Whether the user can modify the account plan.

`AccountManageTeams` - (Optional) Whether the user can modify other teams in the account.

`AccountManageApikeys` - (Optional) Whether the user can modify account apikeys.

`AccountManageAccountSettings` - (Optional) Whether the user can modify account settings.

`AccountViewActivityLog` - (Optional) Whether the user can view activity logs.

`AccountViewInvoices` - (Optional) Whether the user can view invoices.

`MonitoringManageLists` - (Optional) Whether the user can modify notification lists.

`MonitoringManageJobs` - (Optional) Whether the user can modify monitoring jobs.

`MonitoringViewJobs` - (Optional) Whether the user can view monitoring jobs.


## See Also

* [ns1_user](https://www.terraform.io/docs/providers/ns1/r/user.html) in the _Terraform Provider Documentation_
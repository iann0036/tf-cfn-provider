# Terraform::NS1::Team

Provides a NS1 Team resource. This can be used to create, modify, and delete teams.

## Properties

`Name` - (Required) The free form name of the team.

`Permissions` - (Optional) The allowed permissions of the team. Permissions documented below.

### Permissions Properties

`DnsViewZones` - (Optional) Whether the team can view the accounts zones.

`DnsManageZones` - (Optional) Whether the team can modify the accounts zones.

`DnsZonesAllowByDefault` - (Optional) If true, enable the `DnsZonesAllow` list, otherwise enable the `DnsZonesDeny` list.

`DnsZonesAllow` - (Optional) List of zones that the team may access.

`DnsZonesDeny` - (Optional) List of zones that the team may not access.

`DataPushToDatafeeds` - (Optional) Whether the team can publish to data feeds.

`DataManageDatasources` - (Optional) Whether the team can modify data sources.

`DataManageDatafeeds` - (Optional) Whether the team can modify data feeds.

`AccountManageUsers` - (Optional) Whether the team can modify account users.

`AccountManagePaymentMethods` - (Optional) Whether the team can modify account payment methods.

`AccountManagePlan` - (Optional) Whether the team can modify the account plan.

`AccountManageTeams` - (Optional) Whether the team can modify other teams in the account.

`AccountManageApikeys` - (Optional) Whether the team can modify account apikeys.

`AccountManageAccountSettings` - (Optional) Whether the team can modify account settings.

`AccountViewActivityLog` - (Optional) Whether the team can view activity logs.

`AccountViewInvoices` - (Optional) Whether the team can view invoices.

`MonitoringManageLists` - (Optional) Whether the team can modify notification lists.

`MonitoringManageJobs` - (Optional) Whether the team can modify monitoring jobs.

`MonitoringViewJobs` - (Optional) Whether the team can view monitoring jobs.


## See Also

* [ns1_team](https://www.terraform.io/docs/providers/ns1/r/team.html) in the _Terraform Provider Documentation_
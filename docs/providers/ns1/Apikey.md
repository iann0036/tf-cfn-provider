# Terraform::NS1::Apikey

Provides a NS1 Api Key resource. This can be used to create, modify, and delete api keys.

## Properties

`Name` - (Required) The free form name of the apikey.

`Key` - (Required) The apikeys authentication token.

`Teams` - (Required) The teams that the apikey belongs to.

`Permissions` - (Optional) The allowed permissions of the apikey. Permissions documented below.

`DnsViewZones` - (Optional) Whether the apikey can view the accounts zones.

`DnsManageZones` - (Optional) Whether the apikey can modify the accounts zones.

`DnsZonesAllowByDefault` - (Optional) If true, enable the `DnsZonesAllow` list, otherwise enable the `DnsZonesDeny` list.

`DnsZonesAllow` - (Optional) List of zones that the apikey may access.

`DnsZonesDeny` - (Optional) List of zones that the apikey may not access.

`DataPushToDatafeeds` - (Optional) Whether the apikey can publish to data feeds.

`DataManageDatasources` - (Optional) Whether the apikey can modify data sources.

`DataManageDatafeeds` - (Optional) Whether the apikey can modify data feeds.

`AccountManageUsers` - (Optional) Whether the apikey can modify account users.

`AccountManagePaymentMethods` - (Optional) Whether the apikey can modify account payment methods.

`AccountManagePlan` - (Optional) Whether the apikey can modify the account plan.

`AccountManageTeams` - (Optional) Whether the apikey can modify other teams in the account.

`AccountManageApikeys` - (Optional) Whether the apikey can modify account apikeys.

`AccountManageAccountSettings` - (Optional) Whether the apikey can modify account settings.

`AccountViewActivityLog` - (Optional) Whether the apikey can view activity logs.

`AccountViewInvoices` - (Optional) Whether the apikey can view invoices.

`MonitoringManageLists` - (Optional) Whether the apikey can modify notification lists.

`MonitoringManageJobs` - (Optional) Whether the apikey can modify monitoring jobs.

`MonitoringViewJobs` - (Optional) Whether the apikey can view monitoring jobs.


## See Also

* [ns1_apikey](https://www.terraform.io/docs/providers/ns1/r/apikey.html) in the _Terraform Provider Documentation_
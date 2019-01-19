# Terraform::PagerDuty::MaintenanceWindow

A [maintenance window](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Maintenance_Windows/get_maintenance_windows) is used to temporarily disable one or more services for a set period of time. No incidents will be triggered and no notifications will be received while a service is disabled by a maintenance window.

Maintenance windows are specified to start at a certain time and end after they have begun. Once started, a maintenance window cannot be deleted; it can only be ended immediately to re-enable the service.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the maintenance window.

## See Also

* [pagerduty_maintenance_window](https://www.terraform.io/docs/providers/pagerduty/r/maintenance_window.html) in the _Terraform Provider Documentation_
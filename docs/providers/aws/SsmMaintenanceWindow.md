# Terraform::AWS::SsmMaintenanceWindow

Provides an SSM Maintenance Window resource

## Properties

`Name` - (Required) The name of the maintenance window.

`Schedule` - (Required) The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.

`Cutoff` - (Required) The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

`Duration` - (Required) The duration of the Maintenance Window in hours.

`AllowUnassociatedTargets` - (Optional) Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

`Enabled` - (Optional) Whether the maintenance window is enabled. Default: `true`.

`EndDate` - (Optional) Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to no longer run the maintenance window.

`ScheduleTimezone` - (Optional) Timezone for schedule in [Internet Assigned Numbers Authority (IANA) Time Zone Database format](https://www.iana.org/time-zones). For example: `America/Los_Angeles`, `etc/UTC`, or `Asia/Seoul`.

`StartDate` - (Optional) Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to begin the maintenance window.


## Return Values

### Fn::GetAtt

`Id` - The ID of the maintenance window.

## See Also

* [aws_ssm_maintenance_window](https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window.html) in the _Terraform Provider Documentation_
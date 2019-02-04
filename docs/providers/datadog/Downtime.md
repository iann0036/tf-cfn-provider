# Terraform::Datadog::Downtime

Provides a Datadog downtime resource. This can be used to create and manage Datadog downtimes.

## Properties

`Scope` - (Required) A list of items to apply the downtime to, e.g. host:X.

`Active` - (Optional) A flag indicating if the downtime is active now.

`Disabled` - (Optional) A flag indicating if the downtime was disabled.

`Start` - (Optional) POSIX timestamp to start the downtime.

`StartDate` - (Optional) String representing date and time to start the downtime in RFC3339 format.

`End` - (Optional) POSIX timestamp to end the downtime.

`EndDate` - (Optional) String representing date and time to end the downtime in RFC3339 format.

`Recurrence` - (Optional) A dictionary to configure the downtime to be recurring.

`Type` - days, weeks, months, or years.

`Period` - How often to repeat as an integer. For example to repeat every 3 days, select a type of days and a period of 3.

`WeekDays` - (Optional) A list of week days to repeat on. Choose from: Mon, Tue, Wed, Thu, Fri, Sat or Sun. Only applicable when type is weeks. First letter must be capitalized.

`UntilOccurrences` - (Optional) How many times the downtime will be rescheduled. `UntilOccurrences` and `UntilDate` are mutually exclusive.

`UntilDate` - (Optional) The date at which the recurrence should end as a POSIX timestamp. `UntilOccurrences` and `UntilDate` are mutually exclusive.

`Message` - (Optional) A message to include with notifications for this downtime.

`MonitorId` - (Optional) Reference to which monitor this downtime is applied. When scheduling downtime for a given monitor, datadog changes `silenced` property of the monitor  to match the `End` POSIX timestamp.


## Return Values

### Fn::GetAtt

`Id` - ID of the Datadog downtime.

## See Also

* [datadog_downtime](https://www.terraform.io/docs/providers/datadog/r/downtime.html) in the _Terraform Provider Documentation_
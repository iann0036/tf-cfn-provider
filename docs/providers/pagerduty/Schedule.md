# Terraform::PagerDuty::Schedule

A [schedule](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Schedules/get_schedules) determines the time periods that users are on call. Only on-call users are eligible to receive notifications from incidents.

## Properties

`Name` - (Optional) The name of the schedule layer.

`TimeZone` - (Required) The time zone of the schedule (e.g Europe/Berlin).

`Description` - (Optional) The description of the schedule.

`Layer` - (Required) A schedule layer block. Schedule layers documented below.

`Overflow` - (Optional) Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `Overflow` is passed. For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`: If you don't pass the overflow=true parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`. If you do pass the `Overflow` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.

`Start` - (Required) The start time of the schedule layer. This value will not be read back from the PagerDuty API because the API will always return a new `Start` time, which represents the last updated time of the schedule layer.

`End` - (Optional) The end time of the schedule layer. If not specified, the layer does not end.

`RotationVirtualStart` - (Required) The effective start time of the schedule layer. This can be before the start time of the schedule.

`RotationTurnLengthSeconds` - (Required) The duration of each on-call shift in `seconds`.

`Users` - (Required) The ordered list of users on this layer. The position of the user on the list determines their order in the layer.

`Restriction` - (Optional) A schedule layer restriction block. Restriction blocks documented below.

`Type` - (Required) Can be `daily_restriction` or `weekly_restriction`.

`StartTimeOfDay` - (Required) The start time in `HH:mm:ss` format.

`DurationSeconds` - (Required) The duration of the restriction in `seconds`.

`StartDayOfWeek` - (Required for `weekly_restriction`) Number of the day when restriction starts. From 1 to 7 where 1 is Monday and 7 is Sunday.


## Return Values

### Fn::GetAtt

`Id` - The ID of the schedule.

## See Also

* [pagerduty_schedule](https://www.terraform.io/docs/providers/pagerduty/r/schedule.html) in the _Terraform Provider Documentation_
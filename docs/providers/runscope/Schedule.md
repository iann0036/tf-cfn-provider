# Terraform::RunScope::Schedule

A [schedule](https://www.runscope.com/docs/api/schedules) resource.
Tests can be scheduled to run on frequencies up to every minute.
One ore more schedules can be configured per test with each schedule
using a unique Test-specific or Shared [Environment](environment.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the schedule.

## See Also

* [runscope_schedule](https://www.terraform.io/docs/providers/runscope/r/schedule.html) in the _Terraform Provider Documentation_
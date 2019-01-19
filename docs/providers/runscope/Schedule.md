# Terraform::RunScope::Schedule

A [schedule](https://www.runscope.com/docs/api/schedules) resource.
Tests can be scheduled to run on frequencies up to every minute.
One ore more schedules can be configured per test with each schedule
using a unique Test-specific or Shared [Environment](environment.html).

## Properties

`BucketId` - (Required) The id of the bucket to associate this schedule with.

`TestId` - (Required) The id of the test to associate this schedule with.

`EnvironmentId` - (Required) The id of the environment to use when running the test. If given, creates a test specific schedule, otherwise creates a shared schedule.

`Interval` - (Required) The schedule's interval, must be one of: * 1m — every minute * 5m — every 5 minutes * 15m — every 15 minutes * 30m — every 30 minutes * 1h — every hour * 6h — every 6 hours * 1d — every day.

`Note` - (Optional) A human-friendly description for the schedule.


## Return Values

### Fn::GetAtt

`Id` - The ID of the schedule.

## See Also

* [runscope_schedule](https://www.terraform.io/docs/providers/runscope/r/schedule.html) in the _Terraform Provider Documentation_
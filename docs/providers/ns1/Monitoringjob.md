# Terraform::NS1::Monitoringjob

Provides a NS1 Monitoring Job resource. This can be used to create, modify, and delete monitoring jobs.

## Properties

`Name` - (Required) The free-form display name for the monitoring job.

`JobType` - (Required) The type of monitoring job to be run.

`Active` - (Required) Indicates if the job is active or temporaril.y disabled.

`Regions` - (Required) The list of region codes in which to run the monitoring job.

`Frequency` - (Required) The frequency, in seconds, at which to run the monitoring job in each region.

`RapidRecheck` - (Required) If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.

`Policy` - (Required) The policy for determining the monitor's global status based on the status of the job in all regions.

`Config` - (Required) A configuration dictionary with keys and values depending on the jobs' type.

`NotifyDelay` - (Optional) The time in seconds after a failure to wait before sending a notification.

`NotifyRepeat` - (Optional) The time in seconds between repeat notifications of a failed job.

`NotifyFailback` - (Optional) If true, a notification is sent when a job returns to an "up" state.

`NotifyRegional` - (Optional) If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.

`NotifyList` - (Optional) The id of the notification list to send notifications to.

`Notes` - (Optional) Freeform notes to be included in any notifications about this job.

`Rules` - (Optional) A list of rules for determining failure conditions. Job Rules are documented below.

### Rules Properties

`Key` - (Required) The output key.

`Comparison` - (Required) The comparison to perform on the the output.

`Value` - (Required) The value to compare to.


## See Also

* [ns1_monitoringjob](https://www.terraform.io/docs/providers/ns1/r/monitoringjob.html) in the _Terraform Provider Documentation_
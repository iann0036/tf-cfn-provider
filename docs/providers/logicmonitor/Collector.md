# Terraform::LogicMonitor::Collector

Provides a LogicMonitor collector resource. This can be used to create and manage LogicMonitor collectors.

*Note:* This resource will only create the collector device in your account. See [Downloading a Collector Installer](https://www.logicmonitor.com/support/rest-api-developers-guide/collectors/downloading-a-collector-installer/) for
information on how to download and install an existing collector.

## Properties

`BackupCollectorId` - (Optional) The Id of the failover Collector configured for this Collector.

`CollectorGroupId` - (Optional) The Id of the group the Collector is in.

`Description` - (Optional) The Collector's description.

`EnableFailback` - (Optional) Whether or not automatic failback is enabled for the Collector.

`EnableCollectorDeviceFailover` - (Optional) Whether or not the device the Collector is installed on is enabled for fail over.

`EscalationChainId` - (Optional) The Id of the escalation chain associated with this Collector.

`ResendInterval` - (Optional) The interval, in minutes, after which alert notifications for the Collector will be resent.

`SuppressAlertClear` - (Optional) Whether alert clear notifications are suppressed for the Collector.


## See Also

* [logicmonitor_collector](https://www.terraform.io/docs/providers/logicmonitor/r/collector.html) in the _Terraform Provider Documentation_
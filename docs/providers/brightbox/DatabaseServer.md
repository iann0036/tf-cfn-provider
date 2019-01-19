# Terraform::Brightbox::DatabaseServer

Provides a Brightbox Database Server resource. This can be used to create,
modify, and delete Database Servers.

## Properties

`Name` - (Optional) A label assigned to the Database Server.

`Description` - (Optional) A further description of the Database Server.

`MaintenanceWeekday` - (Optional) Numerical index of weekday (0 is Sunday, 1 is Monday...) to set when automatic updates may be performed. Default is 0 (Sunday).

`MaintenanceHour` - (Optional) Number representing 24hr time start of maintenance window hour for x:00-x:59 (0-23). Default is 6.

`DatabaseEngine` - (Optional) Database engine to request. Default is mysql.

`DatabaseVersion` - (Optional) Database version to request. Default is 5.5.

`DatabaseType` - (Optional) ID of the Database Type required.

`Zone` - (Optional) The handle of the zone required (`gb1-a`, `gb1-b`).


## Return Values

### Fn::GetAtt

`Id` - The ID of the Database Server.

`AdminUsername` - The username used to log onto the database.

`AdminPassword` - The password used to log onto the database.

`Status` - Current state of the database server, usually `active` or `deleted`.

`Locked` - True if database server has been set to locked and cannot be deleted.

## See Also

* [brightbox_database_server](https://www.terraform.io/docs/providers/brightbox/r/database_server.html) in the _Terraform Provider Documentation_
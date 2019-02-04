# Terraform::InfluxDB::Database

The database resource allows a database to be created on an InfluxDB server.

## Properties

`Name` - (Required) The name for the database. This must be unique on the
InfluxDB server.

`RetentionPolicies` - (Optional) A list of retention policies for specified database.

### RetentionPolicies Properties

`Name` - (Required) The name of the retention policy.

`Duration` - (Required) The duration for retention policy, format of duration can be found at InfluxDB Documentation.

`Replication` - (Optional) Determines how many copies of data points are stored in a cluster. Not applicable for single node / Open Source version of InfluxDB. Default value of 1.

`Default` - (Optional) Marks current retention policy as default. Default value is false.


## See Also

* [influxdb_database](https://www.terraform.io/docs/providers/influxdb/r/database.html) in the _Terraform Provider Documentation_
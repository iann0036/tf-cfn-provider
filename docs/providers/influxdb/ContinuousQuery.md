# Terraform::InfluxDB::ContinuousQuery

The continuous_query resource allows a continuous query to be created on an InfluxDB server.

## Properties

`Name` - (Required) The name for the continuous_query. This must be unique on the InfluxDB server.

`Database` - (Required) The database for the continuous_query. This must be an existing influxdb database.

`Query` - (Required) The query for the continuous_query.


## See Also

* [influxdb_continuous_query](https://www.terraform.io/docs/providers/influxdb/r/continuous_query.html) in the _Terraform Provider Documentation_
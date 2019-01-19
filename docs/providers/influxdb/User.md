# Terraform::InfluxDB::User

The user resource allows a user to be created on an InfluxDB server.

## Properties

`Name` - (Required) The name for the user.

`Password` - (Required) The password for the user.

`Admin` - (Optional) Mark the user as admin.

`Grant` - (Optional) A list of grants for non-admin users.

### Grant Properties

`Database` - (Required) The name of the database the privilege is associated with.

`Privilege` - (Required) The privilege to grant (READ|WRITE|ALL).


## Return Values

### Fn::GetAtt

`Admin` - (Bool) indication if the user is an admin or not.

## See Also

* [influxdb_user](https://www.terraform.io/docs/providers/influxdb/r/user.html) in the _Terraform Provider Documentation_
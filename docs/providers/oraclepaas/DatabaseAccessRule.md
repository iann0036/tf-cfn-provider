# Terraform::OraclePaaS::DatabaseAccessRule

The `Terraform::OraclePaaS::DatabaseAccessRule` resource creates and manages a Database Access Rule for an Oracle Database Cloud service instance.

## Properties

`Name` - (Required) The name of the Access Rule.

`ServiceInstanceId` - (Required) The name of the database service instance to attach the access rule to.

`Description` - (Required) The description of the Access Rule.

`Ports` - (Required) The port or range of ports to allow traffic on.

`Source` - (Required) The IP addresses and subnets from which traffic is allowed. Valid values are `DB`, `PUBLIC-INTERNET`, or a single IP address or comma-separated list of subnets (in CIDR format) or IPv4 addresses.

`Enabled` - (Optional)  Determines whether the access rule is enabled. Default is `true`.


## See Also

* [oraclepaas_database_access_rule](https://www.terraform.io/docs/providers/oraclepaas/r/database_access_rule.html) in the _Terraform Provider Documentation_
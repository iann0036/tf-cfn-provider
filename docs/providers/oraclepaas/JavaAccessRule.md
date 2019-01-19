# Terraform::OraclePaaS::JavaAccessRule

The `Terraform::OraclePaaS::JavaAccessRule` resource creates and manages an Access Rule for an Java Cloud service instance.

## Properties

`Name` - (Required) The name of the Access Rule.

`ServiceInstanceId` - (Required) The name of the java service instance to attach the access rule to.

`Description` - (Required) The description of the Access Rule.

`Ports` - (Required) The port or range of ports to allow traffic on.

`Destination` - (Required) Destination to which traffic is allowed. Valid values include `WLS_ADMIN`, `WLS_ADMIN_SERVER`, `OTD_ADMIN_HOST`, `OTD`.

`Source` - (Required) The IP addresses and subnets from which traffic is allowed. Valid values include `WLS_ADMIN`, `WLS_ADMIN_SERVER`, `WLS_MANAGED_SERVER`, `OTD_ADMIN_HOST`, `OTD`, or a single IP address or comma-separated list of subnets (in CIDR format) or IPv4 addresses.

`Enabled` - (Optional) Determines whether the access rule is enabled. Default is `true`.

`Protocol` - (Optional) Specifies the communication protocol. Valid values are `tcp` or `udp`. Default is `tcp`.


## See Also

* [oraclepaas_java_access_rule](https://www.terraform.io/docs/providers/oraclepaas/r/java_access_rule.html) in the _Terraform Provider Documentation_
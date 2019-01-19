# Terraform::OraclePaaS::MysqlAccessRule



## Properties

`ServiceInstanceId` - (Required) The name of MySQL instance to attach the access rule to.

`Name` - (Required) Name of the rule.

`Description` - (Optional) Description of the rule.

`Protocol` - (Optional) Communication protocol for the rule. For example, tcp.

`Ports` - (Required) Ports for the rule. This can be a single port or a port range.

`Source` - (Required) The hosts from which traffic is allowed. For example, PUBLIC-INTERNET for any host on the Internet, a single IP address or a comma-separated list of subnets (in CIDR format) or IPv4 addresses.

`Destination` - (Required) The service component to allow traffic to. For example, mysql_MASTER.

`Enabled` - (Optional) Determines whether the access rule is enabled. Valid values are `true` and `false`. The Default is `true`.


## See Also

* [oraclepaas_mysql_access_rule](https://www.terraform.io/docs/providers/oraclepaas/r/mysql_access_rule.html) in the _Terraform Provider Documentation_
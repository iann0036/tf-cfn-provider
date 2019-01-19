# Terraform::Logentries::Log

Provides a Logentries log resource.

## Properties

`LogsetId` - (Required) The id of the `Terraform::Logentries::Logset` resource.

`Name` - (Required) The name of the log. The name should be short and descriptive. For example, Apache Access, Hadoop Namenode.

`Filename` - (Optional) the filename of the log.

`RetentionPeriod` - (Optional, default `ACCOUNT_DEFAULT`) The retention period (`1W`, `2W`, `1M`, `2M`, `6M`, `1Y`, `2Y`, `UNLIMITED`, `ACCOUNT_DEFAULT`).

`Source` - (Optional, default `token`) The log source (`token`, `syslog`, `agent`, `api`). Review the Logentries [log inputs documentation](https://docs.logentries.com/docs/) for more information.

`Type` - (Optional) The log type. See the Logentries [log type documentation](https://logentries.com/doc/log-types/) for more information.


## Return Values

### Fn::GetAtt

`Token` - If the log `Source` is `token`, this value holds the generated log token that is used by logging clients. See the Logentries [token-based input documentation](https://logentries.com/doc/input-token/) for more information.

## See Also

* [logentries_log](https://www.terraform.io/docs/providers/logentries/r/log.html) in the _Terraform Provider Documentation_
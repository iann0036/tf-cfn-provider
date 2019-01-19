# Terraform::UltraDNS::Tcpool

Provides an UltraDNS Traffic Controller pool resource.

## Properties

`Zone` - (Required) The domain to add the record to.

`Name` - (Required) The name of the record.

`Rdata` - (Required) a list of rdata blocks, one for each member in the pool. Record Data documented below.

`Description` - (Required) Description of the Traffic Controller pool. Valid values are strings less than 256 characters.

`Ttl` - (Optional) The TTL of the record. Default: `3600`.

`RunProbes` - (Optional) Boolean to run probes for this pool. Default: `true`.

`ActOnProbes` - (Optional) Boolean to enable and disable pool records when probes are run. Default: `true`.

`MaxToLb` - (Optional) Determines the number of records to balance between. Valid values are integers  `0` - `len(rdata)`. Default: `0`.

`BackupRecordRdata` - (Optional) IPv4 address or CNAME for the backup record. Default: `nil`.

`BackupRecordFailoverDelay` - (Optional) Time in minutes that Traffic Controller waits after detecting that the pool record has failed before activating primary records. Valid values are integers `0` - `30`. Default: `0`.

`Host` - (Required) IPv4 address or CNAME for the pool member.

`FailoverDelay` - (Optional) Time in minutes that Traffic Controller waits after detecting that the pool record has failed before activating secondary records. `0` will activate the secondary records immediately. Integer. Range: `0` - `30`. Default: `0`.

`Priority` - (Optional) Indicates the serving preference for this pool record. Valid values are integers `1` or greater. Default: `1`.

`RunProbes` - (Optional) Whether probes are run for this pool record. Boolean. Default: `true`.

`State` - (Optional) Current state of the pool record. String. Must be one of `"NORMAL"`, `"ACTIVE"`, or `"INACTIVE"`. Default: `"NORMAL"`.

`Threshold` - (Optional) How many probes must agree before the record state is changed. Valid values are integers `1` - `len(probes)`. Default: `1`.

`Weight` - (Optional) Traffic load to send to each server in the Traffic Controller pool. Valid values are integers `2` - `100`. Default: `2`.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Hostname` - The FQDN of the record.

## See Also

* [ultradns_tcpool](https://www.terraform.io/docs/providers/ultradns/r/tcpool.html) in the _Terraform Provider Documentation_
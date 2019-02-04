# Terraform::UltraDNS::ProbePing

Provides an UltraDNS ping probe

## Properties

`Zone` - (Required) The domain of the pool to probe.

`Name` - (Required) The name of the pool to probe.
- `PoolRecord` - (optional) IP address or domain. If provided, a record-level probe is created, otherwise a pool-level probe is created.
- `Agents` - (Required) List of locations that will be used for probing. One or more values must be specified. Valid values are `"NEW_YORK"`, `"PALO_ALTO"`, `"DALLAS"` & `"AMSTERDAM"`.
- `Threshold` - (Required) Number of agents that must agree for a probe state to be changed.
- `PingProbe` - (Required) a Ping Probe block.
- `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`PoolRecord` - (optional) IP address or domain. If provided, a record-level probe is created, otherwise a pool-level probe is created.
- `Agents` - (Required) List of locations that will be used for probing. One or more values must be specified. Valid values are `"NEW_YORK"`, `"PALO_ALTO"`, `"DALLAS"` & `"AMSTERDAM"`.
- `Threshold` - (Required) Number of agents that must agree for a probe state to be changed.
- `PingProbe` - (Required) a Ping Probe block.
- `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Agents` - (Required) List of locations that will be used for probing. One or more values must be specified. Valid values are `"NEW_YORK"`, `"PALO_ALTO"`, `"DALLAS"` & `"AMSTERDAM"`.
- `Threshold` - (Required) Number of agents that must agree for a probe state to be changed.
- `PingProbe` - (Required) a Ping Probe block.
- `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Threshold` - (Required) Number of agents that must agree for a probe state to be changed.
- `PingProbe` - (Required) a Ping Probe block.
- `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`PingProbe` - (Required) a Ping Probe block.
- `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Packets` - (Optional) Number of ICMP packets to send. Default `3`.
- `PacketSize` - (Optional) Size of packets in bytes. Default `56`.
- `Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`PacketSize` - (Optional) Size of packets in bytes. Default `56`.
- `Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`Name` - (Required) Kind of limit. Valid values are `"lossPercent"`, `"total"`, `"average"`, `"run"` & `"avgRun"`.
- `Warning` - (Optional) Amount to trigger a warning.
- `Critical` - (Optional) Amount to trigger a critical.
- `Fail` - (Optional) Amount to trigger a failure.

`Warning` - (Optional) Amount to trigger a warning.
- `Critical` - (Optional) Amount to trigger a critical.
- `Fail` - (Optional) Amount to trigger a failure.

`Critical` - (Optional) Amount to trigger a critical.
- `Fail` - (Optional) Amount to trigger a failure.

`Fail` - (Optional) Amount to trigger a failure.


## See Also

* [ultradns_probe_ping](https://www.terraform.io/docs/providers/ultradns/r/probe_ping.html) in the _Terraform Provider Documentation_
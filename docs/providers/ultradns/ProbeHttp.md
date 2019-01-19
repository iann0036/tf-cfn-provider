# Terraform::UltraDNS::ProbeHttp

Provides an UltraDNS HTTP probe

## Properties

`Zone` - (Required) The domain of the pool to probe.

`Name` - (Required) Kind of limit. Valid values are `"lossPercent"`, `"total"`, `"average"`, `"run"` & `"avgRun"`. - `Warning` - (Optional) Amount to trigger a warning. - `Critical` - (Optional) Amount to trigger a critical. - `Fail` - (Optional) Amount to trigger a failure.

`PoolRecord` - (optional) IP address or domain. If provided, a record-level probe is created, otherwise a pool-level probe is created. - `Agents` - (Required) List of locations that will be used for probing. One or more values must be specified. Valid values are `"NEW_YORK"`, `"PALO_ALTO"`, `"DALLAS"` & `"AMSTERDAM"`. - `Threshold` - (Required) Number of agents that must agree for a probe state to be changed. - `HttpProbe` - (Required) an HTTP Probe block. - `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Agents` - (Required) List of locations that will be used for probing. One or more values must be specified. Valid values are `"NEW_YORK"`, `"PALO_ALTO"`, `"DALLAS"` & `"AMSTERDAM"`. - `Threshold` - (Required) Number of agents that must agree for a probe state to be changed. - `HttpProbe` - (Required) an HTTP Probe block. - `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Threshold` - (Required) Number of agents that must agree for a probe state to be changed. - `HttpProbe` - (Required) an HTTP Probe block. - `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`HttpProbe` - (Required) an HTTP Probe block. - `Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.

`Transaction` - (Optional) One or more Transaction blocks. - `TotalLimits` - (Optional) A Limit block, but with no `Name` attribute.

`TotalLimits` - (Optional) A Limit block, but with no `Name` attribute.

`Method` - (Required) HTTP method. Valid values are`"GET"`, `"POST"`. - `Url` - (Required) URL to probe. - `TransmittedData` - (Optional) Data to send to URL. - `FollowRedirects` - (Optional) Whether to follow redirects. - `Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`Url` - (Required) URL to probe. - `TransmittedData` - (Optional) Data to send to URL. - `FollowRedirects` - (Optional) Whether to follow redirects. - `Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`TransmittedData` - (Optional) Data to send to URL. - `FollowRedirects` - (Optional) Whether to follow redirects. - `Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`FollowRedirects` - (Optional) Whether to follow redirects. - `Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`Limit` - (Required) One or more Limit blocks. Only one limit block may exist for each name.

`Warning` - (Optional) Amount to trigger a warning. - `Critical` - (Optional) Amount to trigger a critical. - `Fail` - (Optional) Amount to trigger a failure.

`Critical` - (Optional) Amount to trigger a critical. - `Fail` - (Optional) Amount to trigger a failure.

`Fail` - (Optional) Amount to trigger a failure.


## See Also

* [ultradns_probe_http](https://www.terraform.io/docs/providers/ultradns/r/probe_http.html) in the _Terraform Provider Documentation_
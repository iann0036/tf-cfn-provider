# Terraform::UltraDNS::ProbeHttp

Provides an UltraDNS HTTP probe

## Properties

`Zone` - (Required) The domain of the pool to probe.

`Name` - (Required) The name of the pool to probe. - `pool_record` - (optional) IP address or domain. If provided, a record-level probe is created, otherwise a pool-level probe is created. - `agents` - (Required) List of locations that will be used for probing. One or more values must be specified. Valid values are `"NEW_YORK"`, `"PALO_ALTO"`, `"DALLAS"` & `"AMSTERDAM"`. - `threshold` - (Required) Number of agents that must agree for a probe state to be changed. - `http_probe` - (Required) an HTTP Probe block. - `interval` - (Optional) Length of time between probes in minutes. Valid values are `"HALF_MINUTE"`, `"ONE_MINUTE"`, `"TWO_MINUTES"`, `"FIVE_MINUTES"`, `"TEN_MINUTES"` & `"FIFTEEN_MINUTE"`. Default: `"FIVE_MINUTES"`.


## See Also

* [ultradns_probe_http](https://www.terraform.io/docs/providers/ultradns/r/probe_http.html) in the _Terraform Provider Documentation_
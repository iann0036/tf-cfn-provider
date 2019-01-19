# Terraform::Circonus::Check

The ``Terraform::Circonus::Check`` resource creates and manages a
[Circonus Check](https://login.circonus.com/resources/api/calls/check_bundle).

~> **NOTE regarding `Terraform::Circonus::Check` vs a Circonus Check Bundle:** The
`Terraform::Circonus::Check` resource is implemented in terms of a
[Circonus Check Bundle](https://login.circonus.com/resources/api/calls/check_bundle).
The `Terraform::Circonus::Check` creates a higher-level abstraction over the implementation
of a Check Bundle.  As such, the naming and structure does not map 1:1 with the
underlying Circonus API.

## Properties

`Active` - (Optional) Whether or not the check is enabled or not (default `true`).

`Caql` - (Optional) A [Circonus Analytics Query Language (CAQL)](https://login.circonus.com/user/docs/CAQL) check.  See below for details on how to configure a `Caql` check.

`Cloudwatch` - (Optional) A [CloudWatch check](https://login.circonus.com/user/docs/Data/CheckTypes/CloudWatch) check. See below for details on how to configure a `Cloudwatch` check.

`Collector` - (Required) A collector ID.  The collector(s) that are responsible for running a `Terraform::Circonus::Check`. The `id` can be the Circonus ID for a Circonus collector (a.k.a. "broker") running in the cloud or an enterprise collector running in your datacenter.  One collection of metrics will be automatically created for each `Collector` specified.

`Consul` - (Optional) A native Consul check.  See below for details on how to configure a `Consul` check.

`Http` - (Optional) A poll-based HTTP check.  See below for details on how to configure the `Http` check.

`Httptrap` - (Optional) An push-based HTTP check.  This check method expects clients to send a specially crafted HTTP JSON payload.  See below for details on how to configure the `Httptrap` check.

`IcmpPing` - (Optional) An ICMP ping check.  See below for details on how to configure the `IcmpPing` check.

`Json` - (Optional) A JSON check.  See below for details on how to configure the `Json` check.

`Metric` - (Required) A list of one or more `Metric` configurations.  All metrics obtained from this check instance will be available as individual metric streams.  See below for a list of supported `Metric` attrbutes.

`MetricLimit` - (Optional) Setting a metric limit will tell the Circonus backend to periodically look at the check to see if there are additional metrics the collector has seen that we should collect. It will not reactivate metrics previously collected and then marked as inactive. Values are `0` to disable, `-1` to enable all metrics or `N+` to collect up to the value `N` (both `-1` and `N+` can not exceed other account restrictions).

`Mysql` - (Optional) A MySQL check.  See below for details on how to configure the `Mysql` check.

`Name` - (Optional) The name of the check that will be displayed in the web interface.

`Notes` - (Optional) Notes about this check.

`Period` - (Optional) The period between each time the check is made in seconds.

`Postgresql` - (Optional) A PostgreSQL check.  See below for details on how to configure the `Postgresql` check.

`Statsd` - (Optional) A statsd check.  See below for details on how to configure the `Statsd` check.

`Tags` - (Optional) A list of tags assigned to this check.

`Target` - (Required) A string containing the location of the thing being checked.  This value changes based on the check type.  For example, for an `Http` check type this would be the URL you're checking. For a DNS check it would be the hostname you wanted to look up.

`Tcp` - (Optional) A TCP check.  See below for details on how to configure the `Tcp` check (includes TLS support).

`Timeout` - (Optional) A floating point number representing the maximum number of seconds this check should wait for a result.  Defaults to `10.0`.


## See Also

* [circonus_check](https://www.terraform.io/docs/providers/circonus/r/check.html) in the _Terraform Provider Documentation_
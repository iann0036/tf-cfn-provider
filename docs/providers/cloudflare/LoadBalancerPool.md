# Terraform::Cloudflare::LoadBalancerPool

Provides a Cloudflare Load Balancer pool resource. This provides a pool of origins that can be used by a Cloudflare Load Balancer. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.

## Properties

`Name` - (Required) A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed.

`Origins` - (Required) The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It's a complex value. See description below.

`CheckRegions` - (Optional) A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found [here](https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions).

`Description` - (Optional) Free text description.

`Enabled` - (Optional) Whether to enable (the default) this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).

`MinimumOrigins` - (Optional) The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.

`Monitor` - (Optional) The ID of the Monitor to use for health checking origins within this pool.

`NotificationEmail` - (Optional) The email address to send health status notifications to. This can be an individual mailbox or a mailing list.

`Name` - (Required) A human-identifiable name for the origin.

`Address` - (Required) The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.

`Weight` - (Optional) The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.

`Enabled` - (Optional) Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.


## Return Values

### Fn::GetAtt

`Id` - ID for this load balancer pool.

`CreatedOn` - The RFC3339 timestamp of when the load balancer was created.

`ModifiedOn` - The RFC3339 timestamp of when the load balancer was last modified.

## See Also

* [cloudflare_load_balancer_pool](https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool.html) in the _Terraform Provider Documentation_
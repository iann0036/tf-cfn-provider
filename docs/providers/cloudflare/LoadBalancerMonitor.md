# Terraform::Cloudflare::LoadBalancerMonitor

If you're using Cloudflare's Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Load balancer monitor ID.

`CreatedOn` - The RFC3339 timestamp of when the load balancer monitor was created.

`ModifiedOn` - The RFC3339 timestamp of when the load balancer monitor was last modified.

## See Also

* [cloudflare_load_balancer_monitor](https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_monitor.html) in the _Terraform Provider Documentation_
# Terraform::Cloudflare::LoadBalancerPool

Provides a Cloudflare Load Balancer pool resource. This provides a pool of origins that can be used by a Cloudflare Load Balancer. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID for this load balancer pool.

`CreatedOn` - The RFC3339 timestamp of when the load balancer was created.

`ModifiedOn` - The RFC3339 timestamp of when the load balancer was last modified.

## See Also

* [cloudflare_load_balancer_pool](https://www.terraform.io/docs/providers/cloudflare/r/load_balancer_pool.html) in the _Terraform Provider Documentation_
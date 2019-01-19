# Terraform::OCI::LoadBalancerPathRouteSet

This resource provides the Path Route Set resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a path route set to a load balancer. For more information, see
[Managing Request Routing](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Name` - The unique name for this set of path route rules. Avoid entering confidential information.  Example: `example_path_route_set`.

`PathRoutes` - The set of path route rules.

`BackendSetName` - The name of the target backend set for requests where the incoming URI matches the specified path.  Example: `example_backend_set`.

`Path` - The path string to match against the incoming URI path.

`PathMatchType` - The type of matching to apply to incoming URIs.

`MatchType` - Specifies how the load balancing service compares a [PathRoute](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute) object's `path` string against the incoming URI.

## See Also

* [oci_load_balancer_path_route_set](https://www.terraform.io/docs/providers/oci/r/load_balancer_path_route_set.html) in the _Terraform Provider Documentation_
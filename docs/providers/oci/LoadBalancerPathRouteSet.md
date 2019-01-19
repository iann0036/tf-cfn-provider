# Terraform::OCI::LoadBalancerPathRouteSet

This resource provides the Path Route Set resource in Oracle Cloud Infrastructure Load Balancer service.

Adds a path route set to a load balancer. For more information, see
[Managing Request Routing](https://docs.cloud.oracle.com/iaas/Content/Balance/Tasks/managingrequest.htm).

## Properties

`LoadBalancerId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer to add the path route set to.

`Name` - (Required) The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering confidential information.  Example: `example_path_route_set`.

`PathRoutes` - (Required) (Updatable) The set of path route rules. * `BackendSetName` - (Required) (Updatable) The name of the target backend set for requests where the incoming URI matches the specified path.  Example: `example_backend_set` * `Path` - (Required) (Updatable) The path string to match against the incoming URI path. *  Path strings are case-insensitive. *  Asterisk (*) wildcards are not supported. *  Regular expressions are not supported.

`BackendSetName` - (Required) (Updatable) The name of the target backend set for requests where the incoming URI matches the specified path.  Example: `example_backend_set` * `Path` - (Required) (Updatable) The path string to match against the incoming URI path. *  Path strings are case-insensitive. *  Asterisk (*) wildcards are not supported. *  Regular expressions are not supported.

`Path` - (Required) (Updatable) The path string to match against the incoming URI path. *  Path strings are case-insensitive. *  Asterisk (*) wildcards are not supported. *  Regular expressions are not supported.

`PathMatchType` - (Required) (Updatable) The type of matching to apply to incoming URIs. * `MatchType` - (Required) (Updatable) Specifies how the load balancing service compares a [PathRoute](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute) object's `Path` string against the incoming URI. *  **EXACT_MATCH** - Looks for a `Path` string that exactly matches the incoming URI path. *  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `Path` string with the best, longest match of the beginning portion of the incoming URI path. *  **PREFIX_MATCH** - Looks for a `Path` string that matches the beginning portion of the incoming URI path. *  **SUFFIX_MATCH** - Looks for a `Path` string that matches the ending portion of the incoming URI path.

`MatchType` - (Required) (Updatable) Specifies how the load balancing service compares a [PathRoute](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute) object's `Path` string against the incoming URI. *  **EXACT_MATCH** - Looks for a `Path` string that exactly matches the incoming URI path. *  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `Path` string with the best, longest match of the beginning portion of the incoming URI path. *  **PREFIX_MATCH** - Looks for a `Path` string that matches the beginning portion of the incoming URI path. *  **SUFFIX_MATCH** - Looks for a `Path` string that matches the ending portion of the incoming URI path.


## Return Values

### Fn::GetAtt

`Name` - The unique name for this set of path route rules. Avoid entering confidential information.  Example: `example_path_route_set`.

`PathRoutes` - The set of path route rules.

`BackendSetName` - The name of the target backend set for requests where the incoming URI matches the specified path.  Example: `example_backend_set`.

`Path` - The path string to match against the incoming URI path.

`PathMatchType` - The type of matching to apply to incoming URIs.

`MatchType` - Specifies how the load balancing service compares a [PathRoute](https://docs.cloud.oracle.com/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute) object's `Path` string against the incoming URI.

## See Also

* [oci_load_balancer_path_route_set](https://www.terraform.io/docs/providers/oci/r/load_balancer_path_route_set.html) in the _Terraform Provider Documentation_
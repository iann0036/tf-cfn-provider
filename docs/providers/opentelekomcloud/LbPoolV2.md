# Terraform::OpenTelekomCloud::LbPoolV2

Manages a V2 pool resource within OpenTelekomCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`Region` argument of the provider is used. Changing this creates a new
pool.

`TenantId` - (Optional) Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.

`Name` - (Optional) Human-readable name for the pool.

`Description` - (Optional) Human-readable description for the pool.

`Protocol` - (Required) The protocol - can either be TCP, HTTP or HTTPS.
Changing this creates a new pool.

`LoadbalancerId` - (Optional) The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

`ListenerId` - (Optional) The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.

`LbMethod` - (Required) The load balancing algorithm to
distribute traffic to the pool's members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.

`Persistence` - Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.

`AdminStateUp` - (Optional) The administrative state of the pool.
A valid value is true (UP) or false (DOWN).

### Persistence Properties

`Type` - (Required) The type of persistence mode. The current specification
supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.

`CookieName` - (Optional) The name of the cookie if persistence mode is set
appropriately. Required if `type = APP_COOKIE`.


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the pool.

`TenantId` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`Protocol` - See Properties above.

`LbMethod` - See Properties above.

`Persistence` - See Properties above.

`AdminStateUp` - See Properties above.

## See Also

* [opentelekomcloud_lb_pool_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_pool_v2.html) in the _Terraform Provider Documentation_
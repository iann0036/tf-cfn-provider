# Terraform::DigitalOcean::Loadbalancer

Provides a DigitalOcean Load Balancer resource. This can be used to create,
modify, and delete Load Balancers.

## Properties

`Name` - (Required) The Load Balancer name.

`Region` - (Required) The region to start in.

`Algorithm` - (Optional) The load balancing algorithm used to determine
which backend Droplet will be selected by a client. It must be either `round_robin`
or `least_connections`. The default value is `round_robin`.

`ForwardingRule` - (Required) A list of `ForwardingRule` to be assigned to the
Load Balancer. The `ForwardingRule` block is documented below.

`Healthcheck` - (Optional) A `Healthcheck` block to be assigned to the
Load Balancer. The `Healthcheck` block is documented below. Only 1 healthcheck is allowed.

`StickySessions` - (Optional) A `StickySessions` block to be assigned to the
Load Balancer. The `StickySessions` block is documented below. Only 1 sticky_sessions block is allowed.

`RedirectHttpToHttps` - (Optional) A boolean value indicating whether
HTTP requests to the Load Balancer on port 80 will be redirected to HTTPS on port 443.
Default value is `false`.

### ForwardingRule Properties

`EntryProtocol` - (Required) The protocol used for traffic to the Load Balancer. The possible values are: `http`, `https`, or `tcp`.

`EntryPort` - (Required) An integer representing the port on which the Load Balancer instance will listen.

`TargetProtocol` - (Required) The protocol used for traffic from the Load Balancer to the backend Droplets. The possible values are: `http`, `https`, or `tcp`.

`TargetPort` - (Required) An integer representing the port on the backend Droplets to which the Load Balancer will send traffic.

`CertificateId` - (Optional) The ID of the TLS certificate to be used for SSL termination.

`TlsPassthrough` - (Optional) A boolean value indicating whether SSL encrypted traffic will be passed through to the backend Droplets. The default value is `false`.

### StickySessions Properties

`Type` - (Required) An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are `cookies` or `none`. If not specified, the default value is `none`.

`CookieName` - (Optional) The name to be used for the cookie sent to the client. This attribute is required when using `cookies` for the sticky sessions type.

`CookieTtlSeconds` - (Optional) The number of seconds until the cookie set by the Load Balancer expires. This attribute is required when using `cookies` for the sticky sessions type.

### Healthcheck Properties

`Protocol` - (Required) The protocol used for health checks sent to the backend Droplets. The possible values are `http` or `tcp`.

`Port` - (Optional) An integer representing the port on the backend Droplets on which the health check will attempt a connection.

`Path` - (Optional) The path on the backend Droplets to which the Load Balancer instance will send a request.

`CheckIntervalSeconds` - (Optional) The number of seconds between between two consecutive health checks. If not specified, the default value is `10`.

`ResponseTimeoutSeconds` - (Optional) The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed. If not specified, the default value is `5`.

`UnhealthyThreshold` - (Optional) The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool. If not specified, the default value is `3`.

`HealthyThreshold` - (Optional) The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool. If not specified, the default value is `5`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Load Balancer.

`Ip` - The ip of the Load Balancer.

## See Also

* [digitalocean_loadbalancer](https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer.html) in the _Terraform Provider Documentation_
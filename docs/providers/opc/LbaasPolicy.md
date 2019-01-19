# Terraform::OPC::LbaasPolicy

The `Terraform::OPC::LbaasPolicy` resource creates and manages a Load Balancer Classic Policy for a Load Balancer Classic instance.

The Policy resource supports the definition of distinct Policy types:

- [Application Cookie Stickiness Policy](#application-cookie-stickiness-policy)
- [CloudGate Policy](#cloudgate-policy)
- [Load Balancer Cookie Stickiness Policy](#load-balancer-cookie-stickiness-policy)
- [Load Balancing Mechanism Policy](#load-balancing-mechanism-policy)
- [Rate Limiting Request Policy](#rate-limiting-request-policy)
- [Redirect Policy](#redirect-policy)
- [Resource Access Control Policy](#resource-access-control-policy)
- [Set Request Header Policy](#set-request-header-policy)
- [SSL Negotiation Policy](#set-negotiation-policy)
- [Trusted Certificate Policy](#trusted-certificate-policy)

## Properties

`Name` - (Required) The name of the Listener.

`LoadBalancer` - (Required) The parent Load Balancer the Listener.

`ApplicationCookieStickinessPolicy` - see [Application Cookie Stickiness Policy](#application-cookie-stickiness-policy).

`CloudgatePolicy` - see [CloudGate Policy](#cloudgate-policy).

`LoadBalancerCookieStickinessPolicy` - see [Load Balancer Cookie Stickiness Policy](#load-balancer-cookie-stickiness-policy).

`LoadBalancingMechanismPolicy` - see [Load Balancing Mechanism Policy](#load-balancing-mechanism-policy).

`RateLimitingRequestPolicy` - see [Rate Limiting Request Policy](#rate-limiting-request-policy).

`RedirectPolicy` - see [Redirect Policy](#redirect-policy).

`ResourceAccessControlPolicy` - see [Resource Access Control Policy](#resource-access-control-policy).

`SetRequestHeaderPolicy` - see [Set Request Header Policy](#set-request-header-policy).

`SslNegotiationPolicy` - see [SSL Negotiation Policy](#set-negotiation-policy).

`TrustedCertificatePolicy` - see [Trusted Certificate Policy](#trusted-certificate-policy).


## See Also

* [opc_lbaas_policy](https://www.terraform.io/docs/providers/opc/r/lbaas_policy.html) in the _Terraform Provider Documentation_
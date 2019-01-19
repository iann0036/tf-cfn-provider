# Terraform::OPC::LbaasPolicy

The `opc_lbaas_policy` resource creates and manages a Load Balancer Classic Policy for a Load Balancer Classic instance.

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

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [opc_lbaas_policy](https://www.terraform.io/docs/providers/opc/r/lbaas_policy.html) in the _Terraform Provider Documentation_
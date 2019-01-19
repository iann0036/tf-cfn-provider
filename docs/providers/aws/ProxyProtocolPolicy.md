# Terraform::AWS::ProxyProtocolPolicy

Provides a proxy protocol policy, which allows an ELB to carry a client connection information to a backend.

## Properties

`LoadBalancer` - (Required) The load balancer to which the policy should be attached.

`InstancePorts` - (Required) List of instance ports to which the policy should be applied. This can be specified if the protocol is SSL or TCP.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

`LoadBalancer` - The load balancer to which the policy is attached.

## See Also

* [aws_proxy_protocol_policy](https://www.terraform.io/docs/providers/aws/r/proxy_protocol_policy.html) in the _Terraform Provider Documentation_
# Terraform::AWS::VpcEndpointService

Provides a VPC Endpoint Service resource.
Service consumers can create an _Interface_ [VPC Endpoint](vpc_endpoint.html) to connect to the service.

~> **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
both a standalone [VPC Endpoint Service Allowed Principal](vpc_endpoint_service_allowed_principal.html) resource
and a VPC Endpoint Service resource with an `AllowedPrincipals` attribute. Do not use the same principal ARN in both
a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
and will overwrite the association.

## Properties

`AcceptanceRequired` - (Required) Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.

`NetworkLoadBalancerArns` - (Required) The ARNs of one or more Network Load Balancers for the endpoint service.

`AllowedPrincipals` - (Optional) The ARNs of one or more principals allowed to discover the endpoint service.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPC endpoint service.

`State` - The state of the VPC endpoint service.

`ServiceName` - The service name.

`ServiceType` - The service type, `Gateway` or `Interface`.

`AvailabilityZones` - The Availability Zones in which the service is available.

`PrivateDnsName` - The private DNS name for the service.

`BaseEndpointDnsNames` - The DNS names for the service.

## See Also

* [aws_vpc_endpoint_service](https://www.terraform.io/docs/providers/aws/r/vpc_endpoint_service.html) in the _Terraform Provider Documentation_
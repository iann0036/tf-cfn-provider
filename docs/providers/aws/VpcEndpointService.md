# Terraform::AWS::VpcEndpointService

Provides a VPC Endpoint Service resource.
Service consumers can create an _Interface_ [VPC Endpoint](vpc_endpoint.html) to connect to the service.

~> **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
both a standalone [VPC Endpoint Service Allowed Principal](vpc_endpoint_service_allowed_principal.html) resource
and a VPC Endpoint Service resource with an `allowed_principals` attribute. Do not use the same principal ARN in both
a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
and will overwrite the association.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the VPC endpoint service.

`State` - The state of the VPC endpoint service.

`ServiceName` - The service name.

`ServiceType` - The service type, `Gateway` or `Interface`.

`AvailabilityZones` - The Availability Zones in which the service is available.

`PrivateDnsName` - The private DNS name for the service.

`BaseEndpointDnsNames` - The DNS names for the service.

## See Also

* [aws_vpc_endpoint_service](https://www.terraform.io/docs/providers/aws/r/vpc_endpoint_service.html) in the _Terraform Provider Documentation_
# Terraform::AWS::VpcEndpointServiceAllowedPrincipal

Provides a resource to allow a principal to discover a VPC endpoint service.

~> **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
both a standalone [VPC Endpoint Service Allowed Principal](vpc_endpoint_service_allowed_principal.html) resource
and a VPC Endpoint Service resource with an `allowed_principals` attribute. Do not use the same principal ARN in both
a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
and will overwrite the association.

## Properties

`VpcEndpointServiceId` - (Required) The ID of the VPC endpoint service to allow permission.

`PrincipalArn` - (Required) The ARN of the principal to allow permissions.


## Return Values

### Fn::GetAtt

`Id` - The ID of the association.

## See Also

* [aws_vpc_endpoint_service_allowed_principal](https://www.terraform.io/docs/providers/aws/r/vpc_endpoint_service_allowed_principal.html) in the _Terraform Provider Documentation_
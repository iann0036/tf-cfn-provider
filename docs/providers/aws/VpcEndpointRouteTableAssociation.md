# Terraform::AWS::VpcEndpointRouteTableAssociation

Manages a VPC Endpoint Route Table Association

## Properties

`RouteTableId` - (Required) Identifier of the EC2 Route Table to be associated with the VPC Endpoint.

`VpcEndpointId` - (Required) Identifier of the VPC Endpoint with which the EC2 Route Table will be associated.


## Return Values

### Fn::GetAtt

`Id` - A hash of the EC2 Route Table and VPC Endpoint identifiers.

## See Also

* [aws_vpc_endpoint_route_table_association](https://www.terraform.io/docs/providers/aws/r/vpc_endpoint_route_table_association.html) in the _Terraform Provider Documentation_
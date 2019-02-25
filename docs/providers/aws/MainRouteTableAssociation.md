# Terraform::AWS::MainRouteTableAssociation

Provides a resource for managing the main routing table of a VPC.

## Properties

`VpcId` - (Required) The ID of the VPC whose main route table should be set.

`RouteTableId` - (Required) The ID of the Route Table to set as the new
main route table for the target VPC.


## Return Values

### Fn::GetAtt

`OriginalRouteTableId` - Used internally, see __Notes__ below.

`Id` - The ID of the Route Table Association.

## See Also

* [aws_main_route_table_association](https://www.terraform.io/docs/providers/aws/r/main_route_table_association.html) in the _Terraform Provider Documentation_
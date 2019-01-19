# Terraform::AWS::RouteTableAssociation

Provides a resource to create an association between a subnet and routing table.

## Properties

`SubnetId` - (Required) The subnet ID to create an association.

`RouteTableId` - (Required) The ID of the routing table to associate with.


## Return Values

### Fn::GetAtt

`Id` - The ID of the association.

## See Also

* [aws_route_table_association](https://www.terraform.io/docs/providers/aws/r/route_table_association.html) in the _Terraform Provider Documentation_
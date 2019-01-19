# Terraform::AWS::VpcPeeringConnectionAccepter

Provides a resource to manage the accepter's side of a VPC Peering Connection.

When a cross-account (requester's AWS account differs from the accepter's AWS account) or an inter-region
VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
accepter's account.
The requester can use the `Terraform::AWS::VpcPeeringConnection` resource to manage its side of the connection
and the accepter can use the `Terraform::AWS::VpcPeeringConnectionAccepter` resource to "adopt" its side of the
connection into management.

## Properties

`VpcPeeringConnectionId` - (Required) The VPC Peering Connection ID to manage.

`AutoAccept` - (Optional) Whether or not to accept the peering request. Defaults to `false`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPC Peering Connection.

`AcceptStatus` - The status of the VPC Peering Connection request.

`VpcId` - The ID of the accepter VPC.

`PeerVpcId` - The ID of the requester VPC.

`PeerOwnerId` - The AWS account ID of the owner of the requester VPC.

`PeerRegion` - The region of the accepter VPC.

`Accepter` - A configuration block that describes [VPC Peering Connection].

`Requester` - A configuration block that describes [VPC Peering Connection].

## See Also

* [aws_vpc_peering_connection_accepter](https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_accepter.html) in the _Terraform Provider Documentation_
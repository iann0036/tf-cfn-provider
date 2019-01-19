# Terraform::HuaweiCloud::VpcPeeringConnectionAccepterV2

Provides a resource to manage the accepter's side of a VPC Peering Connection.

When a cross-tenant (requester's tenant differs from the accepter's tenant) VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
accepter's account.
The requester can use the `huaweicloud_vpc_peering_connection_v2` resource to manage its side of the connection
and the accepter can use the `huaweicloud_vpc_peering_connection_accepter_v2` resource to "adopt" its side of the
connection into management.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Name` - 	The VPC peering connection name.

`Id` - The VPC peering connection ID.

`Status` - The VPC peering connection status.

`VpcId` - The ID of requester VPC involved in a VPC peering connection.

`PeerVpcId` - The VPC ID of the accepter tenant.

`PeerTenantId` - The Tenant Id of the accepter tenant.

## See Also

* [huaweicloud_vpc_peering_connection_accepter_v2](https://www.terraform.io/docs/providers/huaweicloud/r/vpc_peering_connection_accepter_v2.html) in the _Terraform Provider Documentation_
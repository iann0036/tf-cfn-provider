# Terraform::HuaweiCloud::VpcPeeringConnectionV2

Provides a resource to manage a VPC Peering Connection resource.

-> **Note:** For cross-tenant (requester's tenant differs from the accepter's tenant) VPC Peering Connections, use the `huaweicloud_vpc_peering_connection_v2` resource to manage the requester's side of the connection and use the `huaweicloud_vpc_peering_connection_accepter_v2` resource to manage the accepter's side of the connection.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The VPC peering connection ID.

`Status` - The VPC peering connection status. The value can be PENDING_ACCEPTANCE, REJECTED, EXPIRED, DELETED, or ACTIVE.

## See Also

* [huaweicloud_vpc_peering_connection_v2](https://www.terraform.io/docs/providers/huaweicloud/r/vpc_peering_connection_v2.html) in the _Terraform Provider Documentation_
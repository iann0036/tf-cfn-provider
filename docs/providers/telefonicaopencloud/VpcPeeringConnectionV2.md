# Terraform::TelefonicaOpenCloud::VpcPeeringConnectionV2

Provides a resource to manage a VPC Peering Connection resource.

-> **Note:** For cross-tenant (requester's tenant differs from the accepter's tenant) VPC Peering Connections, use the `telefonicaopencloud_vpc_peering_connection_v2` resource to manage the requester's side of the connection and use the `telefonicaopencloud_vpc_peering_connection_accepter_v2` resource to manage the accepter's side of the connection.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The VPC peering connection ID.

`Status` - The VPC peering connection status. The value can be PENDING_ACCEPTANCE, REJECTED, EXPIRED, DELETED, or ACTIVE.

## See Also

* [telefonicaopencloud_vpc_peering_connection_v2](https://www.terraform.io/docs/providers/telefonicaopencloud/r/vpc_peering_connection_v2.html) in the _Terraform Provider Documentation_
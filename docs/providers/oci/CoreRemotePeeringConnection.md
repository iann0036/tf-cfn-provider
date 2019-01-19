# Terraform::OCI::CoreRemotePeeringConnection

This resource provides the Remote Peering Connection resource in Oracle Cloud Infrastructure Core service.

Creates a new remote peering connection (RPC) for the specified DRG.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The OCID of the compartment that contains the RPC.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`DrgId` - The OCID of the DRG that this RPC belongs to.

`Id` - The OCID of the RPC.

`IsCrossTenancyPeering` - Whether the VCN at the other end of the peering is in a different tenancy.  Example: `false`.

`PeerId` - If this RPC is peered, this value is the OCID of the other RPC.

`PeerRegionName` - If this RPC is peered, this value is the region that contains the other RPC.  Example: `us-ashburn-1`.

`PeerTenancyId` - If this RPC is peered, this value is the OCID of the other RPC's tenancy.

`PeeringStatus` - Whether the RPC is peered with another RPC. `NEW` means the RPC has not yet been peered. `PENDING` means the peering is being established. `REVOKED` means the RPC at the other end of the peering has been deleted.

`State` - The RPC's current lifecycle state.

`TimeCreated` - The date and time the RPC was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_core_remote_peering_connection](https://www.terraform.io/docs/providers/oci/r/core_remote_peering_connection.html) in the _Terraform Provider Documentation_
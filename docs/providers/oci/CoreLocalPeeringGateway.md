# Terraform::OCI::CoreLocalPeeringGateway

This resource provides the Local Peering Gateway resource in Oracle Cloud Infrastructure Core service.

Creates a new local peering gateway (LPG) for the specified VCN.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The OCID of the compartment containing the LPG.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The LPG's Oracle ID (OCID).

`IsCrossTenancyPeering` - Whether the VCN at the other end of the peering is in a different tenancy.  Example: `false`.

`PeerAdvertisedCidr` - The smallest aggregate CIDR that contains all the CIDR routes advertised by the VCN at the other end of the peering from this LPG. See `peerAdvertisedCidrDetails` for the individual CIDRs. The value is `null` if the LPG is not peered.  Example: `192.168.0.0/16`, or if aggregated with `172.16.0.0/24` then `128.0.0.0/1`.

`PeerAdvertisedCidrDetails` - The specific ranges of IP addresses available on or via the VCN at the other end of the peering from this LPG. The value is `null` if the LPG is not peered. You can use these as destination CIDRs for route rules to route a subnet's traffic to this LPG.  Example: [`192.168.0.0/16`, `172.16.0.0/24`].

`PeeringStatus` - Whether the LPG is peered with another LPG. `NEW` means the LPG has not yet been peered. `PENDING` means the peering is being established. `REVOKED` means the LPG at the other end of the peering has been deleted.

`PeeringStatusDetails` - Additional information regarding the peering status, if applicable.

`RouteTableId` - The OCID of the route table the LPG is using. For information about why you would associate a route table with an LPG, see [Advanced Scenario: Transit Routing](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm).

`State` - The LPG's current lifecycle state.

`TimeCreated` - The date and time the LPG was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The OCID of the VCN the LPG belongs to.

## See Also

* [oci_core_local_peering_gateway](https://www.terraform.io/docs/providers/oci/r/core_local_peering_gateway.html) in the _Terraform Provider Documentation_
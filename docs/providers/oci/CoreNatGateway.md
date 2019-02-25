# Terraform::OCI::CoreNatGateway

This resource provides the Nat Gateway resource in Oracle Cloud Infrastructure Core service.

Creates a new NAT gateway for the specified VCN. You must also set up a route rule with the
NAT gateway as the rule's target. See [Route Table](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/RouteTable/).

## Properties

`BlockTraffic` - (Optional) (Updatable) Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`.

`CompartmentId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the NAT gateway.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`VcnId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the gateway belongs to.


## Return Values

### Fn::GetAtt

`BlockTraffic` - Whether the NAT gateway blocks traffic through it. The default is `false`.  Example: `true`.

`CompartmentId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the NAT gateway.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the NAT gateway.

`NatIp` - The IP address associated with the NAT gateway.

`State` - The NAT gateway's current state.

`TimeCreated` - The date and time the NAT gateway was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the NAT gateway belongs to.

## See Also

* [oci_core_nat_gateway](https://www.terraform.io/docs/providers/oci/r/core_nat_gateway.html) in the _Terraform Provider Documentation_
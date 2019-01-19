# Terraform::OCI::CoreInternetGateway

This resource provides the Internet Gateway resource in Oracle Cloud Infrastructure Core service.

Creates a new internet gateway for the specified VCN. For more information, see
[Access to the Internet](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want the Internet
Gateway to reside. Notice that the internet gateway doesn't have to be in the same compartment as the VCN or
other Networking Service components. If you're not sure which compartment to use, put the Internet
Gateway in the same compartment with the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the internet gateway, otherwise a default is provided. It
does not have to be unique, and you can change it. Avoid entering confidential information.

For traffic to flow between a subnet and an internet gateway, you must create a route rule accordingly in
the subnet's route table (for example, 0.0.0.0/0 > internet gateway). See
[UpdateRouteTable](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/RouteTable/UpdateRouteTable).

You must specify whether the internet gateway is enabled when you create it. If it's disabled, that means no
traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later
use [UpdateInternetGateway](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/InternetGateway/UpdateInternetGateway) to easily disable/enable
the gateway without changing the route rule.

## Properties

`CompartmentId` - (Required) The OCID of the compartment to contain the internet gateway.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`Enabled` - (Required) (Updatable) Whether the gateway is enabled upon creation.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`VcnId` - (Required) The OCID of the VCN the internet gateway is attached to.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment containing the internet gateway.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`Enabled` - Whether the gateway is enabled. When the gateway is disabled, traffic is not routed to/from the Internet, regardless of route rules.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The internet gateway's Oracle ID (OCID).

`State` - The internet gateway's current state.

`TimeCreated` - The date and time the internet gateway was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The OCID of the VCN the internet gateway belongs to.

## See Also

* [oci_core_internet_gateway](https://www.terraform.io/docs/providers/oci/r/core_internet_gateway.html) in the _Terraform Provider Documentation_
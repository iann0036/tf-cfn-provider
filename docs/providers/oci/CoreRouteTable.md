# Terraform::OCI::CoreRouteTable

This resource provides the Route Table resource in Oracle Cloud Infrastructure Core service.

Creates a new route table for the specified VCN. In the request you must also include at least one route
rule for the new route table. For information on the number of rules you can have in a route table, see
[Service Limits](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). For general information about route
tables in your VCN and the types of targets you can use in route rules,
see [Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want the route
table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets,
or other Networking Service components. If you're not sure which compartment to use, put the route
table in the same compartment as the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the route table, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information on configuring a VCN's default route table, see [Managing Default VCN Resources](/docs/providers/oci/guides/managing_default_resources.html)

## Properties

`CompartmentId` - (Required) The OCID of the compartment to contain the route table.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`RouteRules` - (Required) (Updatable) The collection of rules used for routing destination IPs to network devices. * `CidrBlock` - (Optional) (Updatable) Deprecated. Instead use `Destination` and `destinationType`. Requests that include both `CidrBlock` and `Destination` will be rejected.

`CidrBlock` - (Optional) (Updatable) Deprecated. Instead use `Destination` and `destinationType`. Requests that include both `CidrBlock` and `Destination` will be rejected.

`Destination` - (Optional) (Updatable) Conceptually, this is the range of IP addresses used for matching when routing traffic. Required if you provide a `destinationType`.

`DestinationType` - (Optional) (Updatable) Type of destination for the rule. Required if you provide a `Destination`. * `CIDRBLOCK`: If the rule's `Destination` is an IP address range in CIDR notation. * `SERVICECIDRBLOCK`: If the rule's `Destination` is the `CidrBlock` value for a [Service](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Service/) (the rule is for traffic destined for a particular service through a service gateway). * `NetworkEntityId` - (Required) (Updatable) The OCID for the route rule's target. For information about the type of targets you can specify, see [Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

`NetworkEntityId` - (Required) (Updatable) The OCID for the route rule's target. For information about the type of targets you can specify, see [Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

`VcnId` - (Required) The OCID of the VCN the route table belongs to.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment containing the route table.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The route table's Oracle ID (OCID).

`RouteRules` - The collection of rules for routing destination IPs to network devices.

`CidrBlock` - Deprecated. Instead use `Destination` and `destinationType`. Requests that include both `CidrBlock` and `Destination` will be rejected.

`Destination` - Conceptually, this is the range of IP addresses used for matching when routing traffic. Required if you provide a `destinationType`.

`DestinationType` - Type of destination for the rule. Required if you provide a `Destination`.

`NetworkEntityId` - The OCID for the route rule's target. For information about the type of targets you can specify, see [Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

`State` - The route table's current state.

`TimeCreated` - The date and time the route table was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The OCID of the VCN the route table list belongs to.

## See Also

* [oci_core_route_table](https://www.terraform.io/docs/providers/oci/r/core_route_table.html) in the _Terraform Provider Documentation_
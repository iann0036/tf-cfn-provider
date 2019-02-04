# Terraform::OCI::CoreVirtualCircuit

This resource provides the Virtual Circuit resource in Oracle Cloud Infrastructure Core service.

Creates a new virtual circuit to use with Oracle Cloud
Infrastructure FastConnect. For more information, see
[FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

For the purposes of access control, you must provide the OCID of the
compartment where you want the virtual circuit to reside. If you're
not sure which compartment to use, put the virtual circuit in the
same compartment with the DRG it's using. For more information about
compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the virtual circuit.
It does not have to be unique, and you can change it. Avoid entering confidential information.

**Important:** When creating a virtual circuit, you specify a DRG for
the traffic to flow through. Make sure you attach the DRG to your
VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise
traffic will not flow. For more information, see
[Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

## Properties

`BandwidthShapeName` - (Optional) (Updatable) The provisioned data rate of the connection.  To get a list of the available bandwidth levels (that is, shapes), see [ListFastConnectProviderServiceVirtualCircuitBandwidthShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderVirtualCircuitBandwidthShapes).  Example: `10 Gbps`.

`CompartmentId` - (Required) The OCID of the compartment to contain the virtual circuit.

`CrossConnectMappings` - (Optional) (Updatable) Create a `CrossConnectMapping` for each cross-connect or cross-connect group this virtual circuit will run on.
* `BgpMd5authKey` - (Optional) (Updatable) The key for BGP MD5 authentication. Only applicable if your system requires MD5 authentication. If empty or not set (null), that means you don't use BGP MD5 authentication.
* `CrossConnectOrCrossConnectGroupId` - (Optional) (Updatable) The OCID of the cross-connect or cross-connect group for this mapping. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).
* `CustomerBgpPeeringIp` - (Optional) (Updatable) The BGP IPv4 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv4 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv4 address of the provider's edge router. Must use a /30 or /31 subnet mask.

`BgpMd5authKey` - (Optional) (Updatable) The key for BGP MD5 authentication. Only applicable if your system requires MD5 authentication. If empty or not set (null), that means you don't use BGP MD5 authentication.
* `CrossConnectOrCrossConnectGroupId` - (Optional) (Updatable) The OCID of the cross-connect or cross-connect group for this mapping. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).
* `CustomerBgpPeeringIp` - (Optional) (Updatable) The BGP IPv4 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv4 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv4 address of the provider's edge router. Must use a /30 or /31 subnet mask.

`CrossConnectOrCrossConnectGroupId` - (Optional) (Updatable) The OCID of the cross-connect or cross-connect group for this mapping. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).
* `CustomerBgpPeeringIp` - (Optional) (Updatable) The BGP IPv4 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv4 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv4 address of the provider's edge router. Must use a /30 or /31 subnet mask.

`CustomerBgpPeeringIp` - (Optional) (Updatable) The BGP IPv4 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv4 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv4 address of the provider's edge router. Must use a /30 or /31 subnet mask.

`OracleBgpPeeringIp` - (Optional) (Updatable) The IPv4 address for Oracle's end of the BGP session. Must use a /30 or /31 subnet mask. If the session goes from Oracle to a customer's edge router, the customer specifies this information. If the session goes from Oracle to a provider's edge router, the provider specifies this.

`Vlan` - (Optional) (Updatable) The number of the specific VLAN (on the cross-connect or cross-connect group) that is assigned to this virtual circuit. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).  Example: `200`.

`CustomerBgpAsn` - (Optional) (Updatable) Your BGP ASN (either public or private). Provide this value only if there's a BGP session that goes from your edge router to Oracle. Otherwise, leave this empty or null.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`GatewayId` - (Optional) (Updatable) For private virtual circuits only. The OCID of the [dynamic routing gateway (DRG)](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Drg) that this virtual circuit uses.

`ProviderServiceId` - (Optional) The OCID of the service offered by the provider (if you're connecting via a provider). To get a list of the available service offerings, see [ListFastConnectProviderServices](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderServices).

`PublicPrefixes` - (Optional) For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection.
* `CidrBlock` - (Required) An individual public IP prefix (CIDR) to add to the public virtual circuit. Must be /31 or less specific.

`CidrBlock` - (Required) An individual public IP prefix (CIDR) to add to the public virtual circuit. Must be /31 or less specific.

`Region` - (Optional) The Oracle Cloud Infrastructure region where this virtual circuit is located. Example: `phx`.

`Type` - (Required) The type of IP addresses used in this virtual circuit. PRIVATE means [RFC 1918](https://tools.ietf.org/html/rfc1918) addresses (10.0.0.0/8, 172.16/12, and 192.168/16). Only PRIVATE is supported.


## Return Values

### Fn::GetAtt

`BandwidthShapeName` - The provisioned data rate of the connection.  To get a list of the available bandwidth levels (that is, shapes), see [ListFastConnectProviderServiceVirtualCircuitBandwidthShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderVirtualCircuitBandwidthShapes).  Example: `10 Gbps`.

`BgpManagement` - BGP management option.

`BgpSessionState` - The state of the BGP session associated with the virtual circuit.

`CompartmentId` - The OCID of the compartment containing the virtual circuit.

`CrossConnectMappings` - An array of mappings, each containing properties for a cross-connect or cross-connect group that is associated with this virtual circuit.

`BgpMd5authKey` - The key for BGP MD5 authentication. Only applicable if your system requires MD5 authentication. If empty or not set (null), that means you don't use BGP MD5 authentication.

`CrossConnectOrCrossConnectGroupId` - The OCID of the cross-connect or cross-connect group for this mapping. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).

`CustomerBgpPeeringIp` - The BGP IPv4 address for the router on the other end of the BGP session from Oracle. Specified by the owner of that router. If the session goes from Oracle to a customer, this is the BGP IPv4 address of the customer's edge router. If the session goes from Oracle to a provider, this is the BGP IPv4 address of the provider's edge router. Must use a /30 or /31 subnet mask.

`OracleBgpPeeringIp` - The IPv4 address for Oracle's end of the BGP session. Must use a /30 or /31 subnet mask. If the session goes from Oracle to a customer's edge router, the customer specifies this information. If the session goes from Oracle to a provider's edge router, the provider specifies this.

`Vlan` - The number of the specific VLAN (on the cross-connect or cross-connect group) that is assigned to this virtual circuit. Specified by the owner of the cross-connect or cross-connect group (the customer if the customer is colocated with Oracle, or the provider if the customer is connecting via provider).  Example: `200`.

`CustomerBgpAsn` - The BGP ASN of the network at the other end of the BGP session from Oracle. If the session is between the customer's edge router and Oracle, the value is the customer's ASN. If the BGP session is between the provider's edge router and Oracle, the value is the provider's ASN.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`GatewayId` - The OCID of the customer's [dynamic routing gateway (DRG)](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Drg) that this virtual circuit uses. Applicable only to private virtual circuits.

`Id` - The virtual circuit's Oracle ID (OCID).

`OracleBgpAsn` - The Oracle BGP ASN.

`ProviderServiceId` - The OCID of the service offered by the provider (if the customer is connecting via a provider).

`ProviderState` - The provider's state in relation to this virtual circuit (if the customer is connecting via a provider). ACTIVE means the provider has provisioned the virtual circuit from their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has de-provisioned it.

`PublicPrefixes` - For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection. Each prefix must be /31 or less specific.

`ReferenceComment` - Provider-supplied reference information about this virtual circuit (if the customer is connecting via a provider).

`Region` - The Oracle Cloud Infrastructure region where this virtual circuit is located.

`ServiceType` - Provider service type.

`State` - The virtual circuit's current state. For information about the different states, see [FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

`TimeCreated` - The date and time the virtual circuit was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`Type` - Whether the virtual circuit supports private or public peering. For more information, see [FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

## See Also

* [oci_core_virtual_circuit](https://www.terraform.io/docs/providers/oci/r/core_virtual_circuit.html) in the _Terraform Provider Documentation_
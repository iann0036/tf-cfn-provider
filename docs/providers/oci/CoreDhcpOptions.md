# Terraform::OCI::CoreDhcpOptions

This resource provides the Dhcp Options resource in Oracle Cloud Infrastructure Core service.

Creates a new set of DHCP options for the specified VCN. For more information, see
[DhcpOptions](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/DhcpOptions/).

For the purposes of access control, you must provide the OCID of the compartment where you want the set of
DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN,
subnets, or other Networking Service components. If you're not sure which compartment to use, put the set
of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information on configuring a VCN's default DHCP options, see [Managing Default VCN Resources](/docs/providers/oci/guides/managing_default_resources.html)

## Properties

`CompartmentId` - (Required) The OCID of the compartment to contain the set of DHCP options.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Options` - (Required) (Updatable) A set of DHCP options.

`CustomDnsServers` - (Applicable when type=DomainNameServer) (Updatable) If you set `serverType` to `CustomDnsServer`, specify the IP address of at least one DNS server of your choice (three maximum).

`SearchDomainNames` - (Required when type=SearchDomain) (Updatable) A single search domain name according to [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123). During a DNS query, the OS will append this search domain name to the value being queried.

`ServerType` - (Required when type=DomainNameServer) (Updatable).

`Type` - (Required) (Updatable) The specific DHCP option. Either `DomainNameServer` (for [DhcpDnsOption](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/DhcpDnsOption/)) or `SearchDomain` (for [DhcpSearchDomainOption](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/DhcpSearchDomainOption/)).

`VcnId` - (Required) The OCID of the VCN the set of DHCP options belongs to.


## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment containing the set of DHCP options.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - Oracle ID (OCID) for the set of DHCP options.

`Options` - The collection of individual DHCP options.

`CustomDnsServers` - If you set `serverType` to `CustomDnsServer`, specify the IP address of at least one DNS server of your choice (three maximum).

`SearchDomainNames` - A single search domain name according to [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123). During a DNS query, the OS will append this search domain name to the value being queried.

`Type` - The specific DHCP option. Either `DomainNameServer` (for [DhcpDnsOption](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/DhcpDnsOption/)) or `SearchDomain` (for [DhcpSearchDomainOption](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/DhcpSearchDomainOption/)).

`State` - The current state of the set of DHCP options.

`TimeCreated` - Date and time the set of DHCP options was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The OCID of the VCN the set of DHCP options belongs to.

## See Also

* [oci_core_dhcp_options](https://www.terraform.io/docs/providers/oci/r/core_dhcp_options.html) in the _Terraform Provider Documentation_
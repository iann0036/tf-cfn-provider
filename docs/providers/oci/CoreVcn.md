# Terraform::OCI::CoreVcn

Other supported legacy names/aliases:
  * `Terraform::OCI::CoreVirtualNetwork`

This resource provides the Vcn resource in Oracle Cloud Infrastructure Core service.

The VCN automatically comes with a default route table, default security list, and default set of DHCP options.
For managing these resources, see [Managing Default VCN Resources](/docs/providers/oci/guides/managing_default_resources.html)

Creates a new Virtual Cloud Network (VCN). For more information, see
[VCNs and Subnets](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).

For the VCN you must specify a single, contiguous IPv4 CIDR block. Oracle recommends using one of the
private IP address ranges specified in [RFC 1918](https://tools.ietf.org/html/rfc1918) (10.0.0.0/8,
172.16/12, and 192.168/16). Example: 172.16.0.0/16. The CIDR block can range from /16 to /30, and it
must not overlap with your on-premises network. You can't change the size of the VCN after creation.

For the purposes of access control, you must provide the OCID of the compartment where you want the VCN to
reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which
compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other
Networking Service components. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to
be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the VCN, which is required if you want the instances to use the
Interent and VCN Resolver option for DNS in the VCN. For more information, see
[DNS in Your Virtual Cloud Network](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).

The VCN automatically comes with a default route table, default security list, and default set of DHCP options.
The OCID for each is returned in the response. You can't delete these default objects, but you can change their
contents (that is, change the route rules, security list rules, and so on).

The VCN and subnets you create are not accessible until you attach an internet gateway or set up an IPSec VPN
or FastConnect. For more information, see
[Overview of the Networking Service](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm).

## Properties

`CidrBlock` - (Required) The CIDR IP address block of the VCN.  Example: `172.16.0.0/16`.

`CompartmentId` - (Required) The OCID of the compartment to contain the VCN.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`DnsLabel` - (Optional) A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Not required to be unique, but it's a best practice to set unique DNS labels for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter. The value cannot be changed.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.


## Return Values

### Fn::GetAtt

`CidrBlock` - The CIDR IP address block of the VCN.  Example: `172.16.0.0/16`.

`CompartmentId` - The OCID of the compartment containing the VCN.

`DefaultDhcpOptionsId` - The OCID for the VCN's default set of DHCP options.

`DefaultRouteTableId` - The OCID for the VCN's default route table.

`DefaultSecurityListId` - The OCID for the VCN's default security list.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`DnsLabel` - A DNS label for the VCN, used in conjunction with the VNIC's hostname and subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter. The value cannot be changed.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The VCN's Oracle ID (OCID).

`State` - The VCN's current state.

`TimeCreated` - The date and time the VCN was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnDomainName` - The VCN's domain name, which consists of the VCN's DNS label, and the `oraclevcn.com` domain.

## See Also

* [oci_core_vcn](https://www.terraform.io/docs/providers/oci/r/core_vcn.html) in the _Terraform Provider Documentation_
# Terraform::OCI::CoreSubnet

This resource provides the Subnet resource in Oracle Cloud Infrastructure Core service.

Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation,
so it's important to think about the size of subnets you need before creating them.
For more information, see [VCNs and Subnets](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
For information on the number of subnets you can have in a VCN, see
[Service Limits](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want the subnet
to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or
other Networking Service components. If you're not sure which compartment to use, put the subnet in
the same compartment as the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs,
see [Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally associate a route table with the subnet. If you don't, the subnet will use the
VCN's default route table. For more information about route tables, see
[Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

You may optionally associate a security list with the subnet. If you don't, the subnet will use the
VCN's default security list. For more information about security lists, see
[Security Lists](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securitylists.htm).

You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the
VCN's default set. For more information about DHCP options, see
[DHCP Options](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm).

You may optionally specify a *display name* for the subnet, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the subnet, which is required if you want the Internet and
VCN Resolver to resolve hostnames for instances in the subnet. For more information, see
[DNS in Your Virtual Cloud Network](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AvailabilityDomain` - The subnet's availability domain.  Example: `Uocm:PHX-AD-1`.

`CidrBlock` - The subnet's CIDR block.  Example: `172.16.1.0/24`.

`CompartmentId` - The OCID of the compartment containing the subnet.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DhcpOptionsId` - The OCID of the set of DHCP options that the subnet uses.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`DnsLabel` - A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The subnet's Oracle ID (OCID).

`ProhibitPublicIpOnVnic` - Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet).  Example: `true`.

`RouteTableId` - The OCID of the route table that the subnet uses.

`SecurityListIds` - The OCIDs of the security list or lists that the subnet uses. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.

`State` - The subnet's current state.

`SubnetDomainName` - The subnet's domain name, which consists of the subnet's DNS label, the VCN's DNS label, and the `oraclevcn.com` domain.

`TimeCreated` - The date and time the subnet was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The OCID of the VCN the subnet is in.

`VirtualRouterIp` - The IP address of the virtual router.  Example: `10.0.14.1`.

`VirtualRouterMac` - The MAC address of the virtual router.  Example: `00:00:17:B6:4D:DD`.

## See Also

* [oci_core_subnet](https://www.terraform.io/docs/providers/oci/r/core_subnet.html) in the _Terraform Provider Documentation_
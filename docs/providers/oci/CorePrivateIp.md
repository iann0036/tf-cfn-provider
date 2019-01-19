# Terraform::OCI::CorePrivateIp

This resource provides the Private Ip resource in Oracle Cloud Infrastructure Core service.

Creates a secondary private IP for the specified VNIC.
For more information about secondary private IPs, see
[IP Addresses](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm).

## Properties

TBC

## Return Values

### Fn::GetAtt

`AvailabilityDomain` - The private IP's availability domain.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - The OCID of the compartment containing the private IP.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`HostnameLabel` - The hostname for the private IP. Used for DNS. The value is the hostname portion of the private IP's fully qualified domain name (FQDN) (for example, `bminstance-1` in FQDN `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be unique across all VNICs in the subnet and comply with [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123).

`Id` - The private IP's Oracle ID (OCID).

`IpAddress` - The private IP address of the `privateIp` object. The address is within the CIDR of the VNIC's subnet.  Example: `10.0.3.3`.

`IsPrimary` - Whether this private IP is the primary one on the VNIC. Primary private IPs are unassigned and deleted automatically when the VNIC is terminated.  Example: `true`.

`SubnetId` - The OCID of the subnet the VNIC is in.

`TimeCreated` - The date and time the private IP was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VnicId` - The OCID of the VNIC the private IP is assigned to. The VNIC and private IP must be in the same subnet.

## See Also

* [oci_core_private_ip](https://www.terraform.io/docs/providers/oci/r/core_private_ip.html) in the _Terraform Provider Documentation_
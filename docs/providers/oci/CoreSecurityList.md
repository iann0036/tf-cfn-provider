# Terraform::OCI::CoreSecurityList

This resource provides the Security List resource in Oracle Cloud Infrastructure Core service.

Creates a new security list for the specified VCN. For more information
about security lists, see [Security Lists](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securitylists.htm).
For information on the number of rules you can have in a security list, see
[Service Limits](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want the security
list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets,
or other Networking Service components. If you're not sure which compartment to use, put the security
list in the same compartment as the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the security list, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

For more information on configuring a VCN's default security list, see [Managing Default VCN Resources](/docs/providers/oci/guides/managing_default_resources.html)

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CompartmentId` - The OCID of the compartment containing the security list.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`EgressSecurityRules` - Rules for allowing egress IP packets.

`Destination` - Conceptually, this is the range of IP addresses that a packet originating from the instance can go to.

`DestinationType` - Type of destination for the rule. The default is `CIDR_BLOCK`.

`IcmpOptions` - Optional and valid only for ICMP. Use to specify a particular ICMP type and code as defined in [ICMP Parameters](http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml). If you specify ICMP as the protocol but omit this object, then all ICMP types and codes are allowed. If you do provide this object, the type is required and the code is optional. To enable MTU negotiation for ingress internet traffic, make sure to allow type 3 ("Destination Unreachable") code 4 ("Fragmentation Needed and Don't Fragment was Set"). If you need to specify multiple codes for a single type, create a separate security list rule for each.

`Code` - The ICMP code (optional).

`Type` - The ICMP type.

`Protocol` - The transport protocol. Specify either `all` or an IPv4 protocol number as defined in [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP ("1"), TCP ("6"), and UDP ("17").

`Stateless` - A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if ingress traffic allows TCP destination port 80, there should be an egress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.

`TcpOptions` - Optional and valid only for TCP. Use to specify particular destination ports for TCP rules. If you specify TCP as the protocol but omit this object, then all destination ports are allowed.

`Max` - The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.

`Min` - The minimum port number. Must not be greater than the maximum port number.

`SourcePortRange` - An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.

`UdpOptions` - Optional and valid only for UDP. Use to specify particular destination ports for UDP rules. If you specify UDP as the protocol but omit this object, then all destination ports are allowed.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The security list's Oracle Cloud ID (OCID).

`IngressSecurityRules` - Rules for allowing ingress IP packets.

`Source` - Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.

`SourceType` - Type of source for the rule. The default is `CIDR_BLOCK`.

`State` - The security list's current state.

`TimeCreated` - The date and time the security list was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VcnId` - The OCID of the VCN the security list belongs to.

## See Also

* [oci_core_security_list](https://www.terraform.io/docs/providers/oci/r/core_security_list.html) in the _Terraform Provider Documentation_
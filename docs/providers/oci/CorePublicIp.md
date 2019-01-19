# Terraform::OCI::CorePublicIp

This resource provides the Public Ip resource in Oracle Cloud Infrastructure Core service.

Creates a public IP. Use the `lifetime` property to specify whether it's an ephemeral or
reserved public IP. For information about limits on how many you can create, see
[Public IP Addresses](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).

* **For an ephemeral public IP assigned to a private IP:** You must also specify a `privateIpId`
with the OCID of the primary private IP you want to assign the public IP to. The public IP is
created in the same availability domain as the private IP. An ephemeral public IP must always be
assigned to a private IP, and only to the *primary* private IP on a VNIC, not a secondary
private IP. Exception: If you create a [NatGateway](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/NatGateway/), Oracle
automatically assigns the NAT gateway a regional ephemeral public IP that you cannot remove.

* **For a reserved public IP:** You may also optionally assign the public IP to a private
IP by specifying `privateIpId`. Or you can later assign the public IP with
[UpdatePublicIp](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/PublicIp/UpdatePublicIp).

**Note:** When assigning a public IP to a private IP, the private IP must not already have
a public IP with `lifecycleState` = ASSIGNING or ASSIGNED. If it does, an error is returned.

Also, for reserved public IPs, the optional assignment part of this operation is
asynchronous. Poll the public IP's `lifecycleState` to determine if the assignment
succeeded.

## Properties

TBC

## Return Values

### Fn::GetAtt

`AssignedEntityId` - The OCID of the entity the public IP is assigned to, or in the process of being assigned to.

`AssignedEntityType` - The type of entity the public IP is assigned to, or in the process of being assigned to.

`AvailabilityDomain` - The public IP's availability domain. This property is set only for ephemeral public IPs that are assigned to a private IP (that is, when the `scope` of the public IP is set to AVAILABILITY_DOMAIN). The value is the availability domain of the assigned private IP.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - The OCID of the compartment containing the public IP. For an ephemeral public IP, this is the compartment of its assigned entity (which can be a private IP or a regional entity such as a NAT gateway). For a reserved public IP that is currently assigned, its compartment can be different from the assigned private IP's.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

`Id` - The public IP's Oracle ID (OCID).

`IpAddress` - The public IP address of the `publicIp` object.  Example: `129.146.2.1`.

`Lifetime` - Defines when the public IP is deleted and released back to Oracle's public IP pool.

`PrivateIpId` - Deprecated. Use `assignedEntityId` instead.

`Scope` - Whether the public IP is regional or specific to a particular availability domain.

`State` - The public IP's current state.

`TimeCreated` - The date and time the public IP was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_core_public_ip](https://www.terraform.io/docs/providers/oci/r/core_public_ip.html) in the _Terraform Provider Documentation_
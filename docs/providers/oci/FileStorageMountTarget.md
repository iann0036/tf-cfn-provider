# Terraform::OCI::FileStorageMountTarget

This resource provides the Mount Target resource in Oracle Cloud Infrastructure File Storage service.

Creates a new mount target in the specified compartment and
subnet. You can associate a file system with a mount
target only when they exist in the same availability domain. Instances
can connect to mount targets in another availablity domain, but
you might see higher latency than with instances in the same
availability domain as the mount target.

Mount targets have one or more private IP addresses that you can
provide as the host portion of remote target parameters in
client mount commands. These private IP addresses are listed
in the privateIpIds property of the mount target and are highly available. Mount
targets also consume additional IP addresses in their subnet.
Do not use /30 or smaller subnets for mount target creation because they
do not have sufficient available IP addresses.
Allow at least three IP addresses for each mount target.

For information about access control and compartments, see
[Overview of the IAM
Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

For information about availability domains, see [Regions and
Availability Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
To get a list of availability domains, use the
`ListAvailabilityDomains` operation in the Identity and Access
Management Service API.

All Oracle Cloud Infrastructure Services resources, including
mount targets, get an Oracle-assigned, unique ID called an
Oracle Cloud Identifier (OCID).  When you create a resource,
you can find its OCID in the response. You can also retrieve a
resource's OCID by using a List API operation on that resource
type, or by viewing the resource in the Console.

## Properties

`AvailabilityDomain` - (Required) The availability domain in which to create the mount target.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - (Required) The OCID of the compartment in which to create the mount target.

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - (Optional) (Updatable) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My mount target`.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`HostnameLabel` - (Optional) The hostname for the mount target's IP address, used for DNS resolution. The value is the hostname portion of the private IP address's fully qualified domain name (FQDN). For example, `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`. Must be unique across all VNICs in the subnet and comply with [RFC 952](https://tools.ietf.org/html/rfc952) and [RFC 1123](https://tools.ietf.org/html/rfc1123).

`IpAddress` - (Optional) A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.  Example: `10.0.3.3`.

`SubnetId` - (Required) The OCID of the subnet in which to create the mount target.


## Return Values

### Fn::GetAtt

`AvailabilityDomain` - The availability domain the mount target is in. May be unset as a blank or NULL value.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - The OCID of the compartment that contains the mount target.

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`DisplayName` - A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My mount target`.

`ExportSetId` - The OCID of the associated export set. Controls what file systems will be exported through Network File System (NFS) protocol on this mount target.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Id` - The OCID of the mount target.

`LifecycleDetails` - Additional information about the current 'lifecycleState'.

`PrivateIpIds` - The OCIDs of the private IP addresses associated with this mount target.

`State` - The current state of the mount target.

`SubnetId` - The OCID of the subnet the mount target is in.

`TimeCreated` - The date and time the mount target was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_file_storage_mount_target](https://www.terraform.io/docs/providers/oci/r/file_storage_mount_target.html) in the _Terraform Provider Documentation_
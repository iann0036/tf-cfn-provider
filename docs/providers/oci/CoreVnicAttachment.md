# Terraform::OCI::CoreVnicAttachment

This resource provides the Vnic Attachment resource in Oracle Cloud Infrastructure Core service.

Creates a secondary VNIC and attaches it to the specified instance.
For more information about secondary VNICs, see
[Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`AvailabilityDomain` - The availability domain of the instance.  Example: `Uocm:PHX-AD-1`.

`CompartmentId` - The OCID of the compartment the VNIC attachment is in, which is the same compartment the instance is in.

`DisplayName` - A user-friendly name. Does not have to be unique. Avoid entering confidential information.

`Id` - The OCID of the VNIC attachment.

`InstanceId` - The OCID of the instance.

`NicIndex` - Which physical network interface card (NIC) the VNIC uses. Certain bare metal instance shapes have two active physical NICs (0 and 1). If you add a secondary VNIC to one of these instances, you can specify which NIC the VNIC will use. For more information, see [Virtual Network Interface Cards (VNICs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm).

`State` - The current state of the VNIC attachment.

`SubnetId` - The OCID of the VNIC's subnet.

`TimeCreated` - The date and time the VNIC attachment was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`VlanTag` - The Oracle-assigned VLAN tag of the attached VNIC. Available after the attachment process is complete.  Example: `0`.

`VnicId` - The OCID of the VNIC. Available after the attachment process is complete.

## See Also

* [oci_core_vnic_attachment](https://www.terraform.io/docs/providers/oci/r/core_vnic_attachment.html) in the _Terraform Provider Documentation_
# Terraform::OCI::FileStorageSnapshot

This resource provides the Snapshot resource in Oracle Cloud Infrastructure File Storage service.

Creates a new snapshot of the specified file system. You
can access the snapshot at `.snapshot/<name>`.

## Properties

`DefinedTags` - (Optional) (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`FileSystemId` - (Required) The OCID of the file system to take a snapshot of.

`FreeformTags` - (Optional) (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Name` - (Required) Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.


## Return Values

### Fn::GetAtt

`DefinedTags` - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`.

`FileSystemId` - The OCID of the file system from which the snapshot was created.

`FreeformTags` - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`.

`Id` - The OCID of the snapshot.

`Name` - Name of the snapshot. This value is immutable.

`State` - The current state of the snapshot.

`TimeCreated` - The date and time the snapshot was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`.

## See Also

* [oci_file_storage_snapshot](https://www.terraform.io/docs/providers/oci/r/file_storage_snapshot.html) in the _Terraform Provider Documentation_
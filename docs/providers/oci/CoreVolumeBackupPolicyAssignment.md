# Terraform::OCI::CoreVolumeBackupPolicyAssignment

This resource provides the Volume Backup Policy Assignment resource in Oracle Cloud Infrastructure Core service.

Assigns a policy to the specified asset, such as a volume. Note that a given asset can
only have one policy assigned to it; if this method is called for an asset that previously
has a different policy assigned, the prior assignment will be silently deleted.

## Properties

TBC

## Return Values

### Fn::GetAtt

`AssetId` - The OCID of the asset (e.g. a volume) to which the policy has been assigned.

`Id` - The OCID of the volume backup policy assignment.

`PolicyId` - The OCID of the volume backup policy that has been assigned to an asset.

`TimeCreated` - The date and time the volume backup policy assignment was created. Format defined by RFC3339.

## See Also

* [oci_core_volume_backup_policy_assignment](https://www.terraform.io/docs/providers/oci/r/core_volume_backup_policy_assignment.html) in the _Terraform Provider Documentation_
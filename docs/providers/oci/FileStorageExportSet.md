# Terraform::OCI::FileStorageExportSet

This resource provides the Export Set resource in Oracle Cloud Infrastructure File Storage service.

The export set resource can neither be directly created, nor destroyed.

An export set is created by the service automatically when a mount target is created.
When a mount target is deleted, the export set associated with it is also deleted automatically.

However, export sets expose a few attributes that can be updated.

Hence we provide this resource for managing the already created export set from within Terraform.

## Properties

`MountTargetId` - (Required) (Updatable) The OCID of the mount target that the export set is associated with.

`DisplayName` - (Optional) (Updatable) A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My export set`.

`MaxFsStatBytes` - (Optional) (Updatable) Controls the maximum `tbytes`, `fbytes`, and `abytes`, values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tbytes` value reported by `FSSTAT` will be `maxFsStatBytes`. The value of `fbytes` and `abytes` will be `maxFsStatBytes` minus the metered size of the file system. If the metered size is larger than `maxFsStatBytes`, then `fbytes` and `abytes` will both be '0'.

`MaxFsStatFiles` - (Optional) (Updatable) Controls the maximum `tfiles`, `ffiles`, and `afiles` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tfiles` value reported by `FSSTAT` will be `maxFsStatFiles`. The value of `ffiles` and `afiles` will be `maxFsStatFiles` minus the metered size of the file system. If the metered size is larger than `maxFsStatFiles`, then `ffiles` and `afiles` will both be '0'.


## Return Values

### Fn::GetAtt

`MaxFsStatFiles` - Controls the maximum `tfiles`, `ffiles`, and `afiles` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tfiles` value reported by `FSSTAT` will be `maxFsStatFiles`. The value of `ffiles` and `afiles` will be `maxFsStatFiles` minus the metered size of the file system. If the metered size is larger than `maxFsStatFiles`, then `ffiles` and `afiles` will both be '0'.

`VcnId` - The OCID of the virtual cloud network (VCN) the export set is in.

`AvailabilityDomain` - The availability domain the export set is in. May be unset as a blank or NULL value.  Example: `Uocm:PHX-AD-1`.

`DisplayName` - A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My export set`.

`CompartmentId` - The OCID of the compartment that contains the export set.

`TimeCreated` - The date and time the export set was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`.

`State` - The current state of the export set.

`MaxFsStatBytes` - Controls the maximum `tbytes`, `fbytes`, and `abytes`, values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tbytes` value reported by `FSSTAT` will be `maxFsStatBytes`. The value of `fbytes` and `abytes` will be `maxFsStatBytes` minus the metered size of the file system. If the metered size is larger than `maxFsStatBytes`, then `fbytes` and `abytes` will both be '0'.

`Id` - The OCID of the export set.

## See Also

* [oci_file_storage_export_set](https://www.terraform.io/docs/providers/oci/r/file_storage_export_set.html) in the _Terraform Provider Documentation_
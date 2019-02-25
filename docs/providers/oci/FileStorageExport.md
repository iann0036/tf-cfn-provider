# Terraform::OCI::FileStorageExport

This resource provides the Export resource in Oracle Cloud Infrastructure File Storage service.

Creates a new export in the specified export set, path, and
file system.

## Properties

`ExportOptions` - (Optional) (Updatable) Export options for the new export. If left unspecified, defaults to:.

### ExportOptions Properties

`Access` - (Optional) (Updatable) Type of access to grant clients using the file system through this export. If unspecified defaults to `READ_ONLY`.
* `AnonymousGid` - (Optional) (Updatable) GID value to remap to when squashing a client GID (see identitySquash for more details.) If unspecified defaults to `65534`.
* `AnonymousUid` - (Optional) (Updatable) UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.
* `IdentitySquash` - (Optional) (Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `RequirePrivilegedSourcePort` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `Source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

`AnonymousGid` - (Optional) (Updatable) GID value to remap to when squashing a client GID (see identitySquash for more details.) If unspecified defaults to `65534`.
* `AnonymousUid` - (Optional) (Updatable) UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.
* `IdentitySquash` - (Optional) (Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `RequirePrivilegedSourcePort` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `Source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

`AnonymousUid` - (Optional) (Updatable) UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.
* `IdentitySquash` - (Optional) (Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `RequirePrivilegedSourcePort` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `Source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

`IdentitySquash` - (Optional) (Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `RequirePrivilegedSourcePort` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `Source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

`RequirePrivilegedSourcePort` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `Source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

`Source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

`ExportSetId` - (Required) The OCID of this export's export set.

`FileSystemId` - (Required) The OCID of this export's file system.

`Path` - (Required) Path used to access the associated file system.


## Return Values

### Fn::GetAtt

`FileSystemId` - The OCID of this export's file system.

`ExportSetId` - The OCID of this export's export set.

`TimeCreated` - The date and time the export was created, expressed in [RFC 3339](https://tools.ietf.org/rfc/rfc3339) timestamp format.  Example: `2016-08-25T21:10:29.600Z`.

`Access` - Type of access to grant clients using the file system through this export. If unspecified defaults to `READ_ONLY`.

`Source` - Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

`State` - The current state of this export.

`RequirePrivilegedSourcePort` - If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.

`IdentitySquash` - Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.

`AnonymousGid` - GID value to remap to when squashing a client GID (see identitySquash for more details.) If unspecified defaults to `65534`.

`AnonymousUid` - UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.

`Path` - Path used to access the associated file system.

`ExportOptions` - Policies that apply to NFS requests made through this export. `exportOptions` contains a sequential list of `ClientOptions`. Each `ClientOptions` item defines the export options that are applied to a specified set of clients.

`Id` - The OCID of this export.

## See Also

* [oci_file_storage_export](https://www.terraform.io/docs/providers/oci/r/file_storage_export.html) in the _Terraform Provider Documentation_
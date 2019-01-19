# Terraform::AWS::DatasyncLocationNfs

Manages an NFS Location within AWS DataSync.

~> **NOTE:** The DataSync Agents must be available before creating this resource.

## Properties

`OnPremConfig` - (Required) Configuration block containing information for connecting to the NFS File System.

`ServerHostname` - (Required) Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.

`Subdirectory` - (Required) Subdirectory to perform actions as source or destination. Should be exported by the NFS server.

`Tags` - (Optional) Key-value pairs of resource tags to assign to the DataSync Location.


## See Also

* [aws_datasync_location_nfs](https://www.terraform.io/docs/providers/aws/r/datasync_location_nfs.html) in the _Terraform Provider Documentation_
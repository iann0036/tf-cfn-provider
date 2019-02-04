# Terraform::VSphere::File

The `Terraform::VSphere::File` resource can be used to upload files (such as virtual disk
files) from the host machine that Terraform is running on to a target
datastore.  The resource can also be used to copy files between datastores, or
from one location to another on the same datastore.

Updates to destination parameters such as `Datacenter`, `Datastore`, or
`DestinationFile` will move the managed file a new destination based on the
values of the new settings.  If any source parameter is changed, such as
`SourceDatastore`, `SourceDatacenter` or `SourceFile`), the resource will be
re-created. Depending on if destination parameters are being changed as well,
this may result in the destination file either being overwritten or deleted at
the old location.

## Properties

`SourceFile` - (Required) The path to the file being uploaded from the
Terraform host to vSphere or copied within vSphere. Forces a new resource if
changed.

`DestinationFile` - (Required) The path to where the file should be uploaded
or copied to on vSphere.

`SourceDatacenter` - (Optional) The name of a datacenter in which the file
will be copied from. Forces a new resource if changed.

`Datacenter` - (Optional) The name of a datacenter in which the file will be
uploaded to.

`SourceDatastore` - (Optional) The name of the datastore in which file will
be copied from. Forces a new resource if changed.

`Datastore` - (Required) The name of the datastore in which to upload the
file to.

`CreateDirectories` - (Optional) Create directories in `DestinationFile`
path parameter if any missing for copy operation.


## See Also

* [vsphere_file](https://www.terraform.io/docs/providers/vsphere/r/file.html) in the _Terraform Provider Documentation_
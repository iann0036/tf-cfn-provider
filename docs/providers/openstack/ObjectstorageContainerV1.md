# Terraform::OpenStack::ObjectstorageContainerV1

Manages a V1 container resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to create the container. If
omitted, the `Region` argument of the provider is used. Changing this
creates a new container.

`Name` - (Required) A unique name for the container. Changing this creates a
new container.

`ContainerRead` - (Optional) Sets an access control list (ACL) that grants
read access. This header can contain a comma-delimited list of users that
can read the container (allows the GET method for all objects in the
container). Changing this updates the access control list read access.

`ContainerSyncTo` - (Optional) The destination for container synchronization.
Changing this updates container synchronization.

`ContainerSyncKey` - (Optional) The secret key for container synchronization.
Changing this updates container synchronization.

`ContainerWrite` - (Optional) Sets an ACL that grants write access.
Changing this updates the access control list write access.

`Versioning` - (Optional) Enable object versioning. The structure is described below.

`Metadata` - (Optional) Custom key/value pairs to associate with the container.
Changing this updates the existing container metadata.

`ContentType` - (Optional) The MIME type for the container. Changing this
updates the MIME type.

`ForceDestroy` -  (Optional, Default:false ) A boolean that indicates all objects should be deleted from the container so that the container can be destroyed without error. These objects are not recoverable.

### Versioning Properties

`Type` - (Required) Versioning type which can be `versions` or `history` according to [Openstack documentation](https://docs.openstack.org/swift/latest/overview_object_versioning.html).

`Location` - (Required) Container in which versions will be stored.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`ContainerRead` - See Properties above.

`ContainerSyncTo` - See Properties above.

`ContainerSyncKey` - See Properties above.

`ContainerWrite` - See Properties above.

`Versioning` - See Properties above.

`Metadata` - See Properties above.

`ContentType` - See Properties above.

## See Also

* [openstack_objectstorage_container_v1](https://www.terraform.io/docs/providers/openstack/r/objectstorage_container_v1.html) in the _Terraform Provider Documentation_
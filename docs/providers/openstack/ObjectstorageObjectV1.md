# Terraform::OpenStack::ObjectstorageObjectV1

Manages a V1 container object resource within OpenStack.

## Properties

`ContainerName` - (Required) A unique (within an account) name for the container.
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.

`Content` - (Optional) A string representing the content of the object. Conflicts with
`Source` and `CopyFrom`.

`ContentDisposition` - (Optional) A string which specifies the override behavior for
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.

`ContentEncoding` - (Optional) A string representing the value of the Content-Encoding
metadata.

`ContentType` - (Optional) A string which sets the MIME type for the object.

`CopyFrom` - (Optional) A string representing the name of an object
used to create the new object by copying the `CopyFrom` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `Source` and
`Content`.

`DeleteAfter` - (Optional) An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.

`DeleteAt` - (Optional) An string representing the date when the system removes the object.
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.

`DetectContentType` - (Optional) If set to true, Object Storage guesses the content
type based on the file extension and ignores the value sent in the Content-Type
header, if present.

`Etag` - (Optional) Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.

`Name` - (Required) A unique name for the object.

`ObjectManifest` - (Optional) A string set to specify that this is a dynamic large
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.

`Region` - (Optional) The region in which to create the container. If
omitted, the `Region` argument of the provider is used. Changing this
creates a new container.

`Source` - (Optional) A string representing the local path of a file which will be used
as the object's content. Conflicts with `Source` and `CopyFrom`.


## Return Values

### Fn::GetAtt

`ContentLength` - If the operation succeeds, this value is zero (0) or the.

`ContentType` - If the operation succeeds, this value is the MIME type of the object.

`Date` - The date and time the system responded to the request, using the preferred.

`Etag` - Whatever the value given in argument, will be overriden by the MD5 checksum of the uploaded object content. The value is not quoted.

`LastModified` - The date and time when the object was last modified. The date and time.

`StaticLargeObject` - True if object is a multipart_manifest.

`TransId` - A unique transaction ID for this request. Your service provider might.

`ContainerName` - See Properties above.

`Content` - See Properties above.

`ContentDisposition` - See Properties above.

`ContentEncoding` - See Properties above.

`CopyFrom` - See Properties above.

`DeleteAfter` - See Properties above.

`DeleteAt` - See Properties above.

`DetectContentType` - See Properties above.

`Name` - See Properties above.

`ObjectManifest` - See Properties above.

`Region` - See Properties above.

`Source` - See Properties above.

## See Also

* [openstack_objectstorage_object_v1](https://www.terraform.io/docs/providers/openstack/r/objectstorage_object_v1.html) in the _Terraform Provider Documentation_
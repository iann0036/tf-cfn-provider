# Terraform::OCI::ObjectstorageObject

This resource provides the Object resource in Oracle Cloud Infrastructure Object Storage service.

Creates a new object or overwrites an existing one.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Bucket` - The name of the bucket for the source object.

`Content` - The object to upload to the object store.

`ContentEncoding` - The content encoding of the object.

`ContentLanguage` - The content language of the object.

`ContentLength` - The content length of the body.

`ContentMd5` - The base-64 encoded MD5 hash of the body.

`ContentType` - The content type of the object.  Defaults to 'application/octet-stream' if not overridden during the PutObject call.

`Metadata` - Optional user-defined metadata key and value.

`Namespace` - The top-level namespace of the source object.

`Object` - The name of the source object.

`Source` - An absolute path to a file on the local system to upload to the object store.

`SourceUriDetails` - Details of the source URI of the object in the cloud.

`Region` - The region of the source object.

## See Also

* [oci_objectstorage_object](https://www.terraform.io/docs/providers/oci/r/objectstorage_object.html) in the _Terraform Provider Documentation_
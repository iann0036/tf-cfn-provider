# Terraform::OCI::ObjectstorageObject

This resource provides the Object resource in Oracle Cloud Infrastructure Object Storage service.

Creates a new object or overwrites an existing one.

## Properties

`Bucket` - (Required) The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`.

`ContentEncoding` - (Optional) The content encoding of the object.

`ContentLanguage` - (Optional) The content language of the object.

`ContentType` - (Optional) The content type of the object.  Defaults to 'application/octet-stream' if not overridden during the PutObject call.

`Content` - (Required) The object to upload to the object store. Cannot be defined if `Source` or `SourceUriDetails` is defined.

`Metadata` - (Optional) Optional user-defined metadata key and value. Note: All specified keys must be in lower case.

`Namespace` - (Required) The top-level namespace used for the request.

`Object` - (Required) The name of the object. Avoid entering confidential information. Example: `test/object1.log`.

`Source` - (Optional) An absolute path to a file on the local system. Cannot be defined if `Content` or `SourceUriDetails` is defined.

`SourceUriDetails` - (Optional) Details of the source URI of the object in the cloud. Cannot be defined if `Content` or `Source` is defined. Note: To enable object copy, you must authorize the service to manage objects on your behalf. * `Region` - (Required) The region of the source object. * `Namespace` - (Required) The top-level namespace of the source object. * `Bucket` - (Required) The name of the bucket for the source object. * `Object` - (Required) The name of the source object. * `SourceObjectIfMatchEtag` - (Optional) The entity tag to match the source object. * `DestinationObjectIfMatchEtag` - (Optional) The entity tag to match the target object. * `DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.

`Region` - (Required) The region of the source object. * `Namespace` - (Required) The top-level namespace of the source object. * `Bucket` - (Required) The name of the bucket for the source object. * `Object` - (Required) The name of the source object. * `SourceObjectIfMatchEtag` - (Optional) The entity tag to match the source object. * `DestinationObjectIfMatchEtag` - (Optional) The entity tag to match the target object. * `DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.

`Namespace` - (Required) The top-level namespace of the source object. * `Bucket` - (Required) The name of the bucket for the source object. * `Object` - (Required) The name of the source object. * `SourceObjectIfMatchEtag` - (Optional) The entity tag to match the source object. * `DestinationObjectIfMatchEtag` - (Optional) The entity tag to match the target object. * `DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.

`Bucket` - (Required) The name of the bucket for the source object. * `Object` - (Required) The name of the source object. * `SourceObjectIfMatchEtag` - (Optional) The entity tag to match the source object. * `DestinationObjectIfMatchEtag` - (Optional) The entity tag to match the target object. * `DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.

`Object` - (Required) The name of the source object. * `SourceObjectIfMatchEtag` - (Optional) The entity tag to match the source object. * `DestinationObjectIfMatchEtag` - (Optional) The entity tag to match the target object. * `DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.

`SourceObjectIfMatchEtag` - (Optional) The entity tag to match the source object. * `DestinationObjectIfMatchEtag` - (Optional) The entity tag to match the target object. * `DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.

`DestinationObjectIfMatchEtag` - (Optional) The entity tag to match the target object. * `DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.

`DestinationObjectIfNoneMatchEtag` - (Optional) The entity tag to not match the target object.


## Return Values

### Fn::GetAtt

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
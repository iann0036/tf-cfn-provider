# Terraform::Google::StorageBucketObject

Creates a new object inside an existing bucket in Google cloud storage service (GCS). 
[ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied using the `Terraform::Google::StorageObjectAcl` resource.
 For more information see 
[the official documentation](https://cloud.google.com/storage/docs/key-terms#objects) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/objects).

## Properties

`Bucket` - (Required) The name of the containing bucket.

`Name` - (Required) The name of the object.

`Content` - (Optional) Data as `string` to be uploaded. Must be defined if `Source` is not.

`Source` - (Optional) A path to the data you want to upload. Must be defined if `Content` is not.

`CacheControl` - (Optional) [Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2) directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600.

`ContentDisposition` - (Optional) [Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.

`ContentEncoding` - (Optional) [Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.

`ContentLanguage` - (Optional) [Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.

`ContentType` - (Optional) [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".

`StorageClass` - (Optional) The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`. If not provided, this defaults to the bucket's default storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.


## Return Values

### Fn::GetAtt

`Crc32c` - (Computed) Base 64 CRC32 hash of the uploaded data.

`Md5hash` - (Computed) Base 64 MD5 hash of the uploaded data.

`SelfLink` - (Computed) A url reference to this object.

## See Also

* [google_storage_bucket_object](https://www.terraform.io/docs/providers/google/r/storage_bucket_object.html) in the _Terraform Provider Documentation_
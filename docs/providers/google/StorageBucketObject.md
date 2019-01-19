# Terraform::Google::StorageBucketObject

Creates a new object inside an existing bucket in Google cloud storage service (GCS). 
[ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied using the `google_storage_object_acl` resource.
 For more information see 
[the official documentation](https://cloud.google.com/storage/docs/key-terms#objects) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/objects).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Crc32c` - (Computed) Base 64 CRC32 hash of the uploaded data.

`Md5hash` - (Computed) Base 64 MD5 hash of the uploaded data.

`SelfLink` - (Computed) A url reference to this object.

## See Also

* [google_storage_bucket_object](https://www.terraform.io/docs/providers/google/r/storage_bucket_object.html) in the _Terraform Provider Documentation_
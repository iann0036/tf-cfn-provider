# Terraform::Google::StorageBucketAcl

Creates a new bucket ACL in Google cloud storage service (GCS). For more information see 
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls).

## Properties

`Bucket` - (Required) The name of the bucket it applies to.

`PredefinedAcl` - (Optional) The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `RoleEntity` is not.

`RoleEntity` - (Optional) List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `PredefinedAcl` is not.

`DefaultAcl` - (Optional) Configure this ACL to be the default ACL.


## See Also

* [google_storage_bucket_acl](https://www.terraform.io/docs/providers/google/r/storage_bucket_acl.html) in the _Terraform Provider Documentation_
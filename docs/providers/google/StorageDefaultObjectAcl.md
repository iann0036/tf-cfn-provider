# Terraform::Google::StorageDefaultObjectAcl

Authoritatively manages the default object ACLs for a Google Cloud Storage bucket
without managing the bucket itself.

-> Note that for each object, its creator will have the `"OWNER"` role in addition
to the default ACL that has been defined.

For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls).

-> Want fine-grained control over default object ACLs? Use `google_storage_default_object_access_control`
to control individual role entity pairs.

## Properties

TBC

## See Also

* [google_storage_default_object_acl](https://www.terraform.io/docs/providers/google/r/storage_default_object_acl.html) in the _Terraform Provider Documentation_
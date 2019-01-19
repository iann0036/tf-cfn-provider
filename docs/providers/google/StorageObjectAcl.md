# Terraform::Google::StorageObjectAcl

Authoritatively manages the access control list (ACL) for an object in a Google
Cloud Storage (GCS) bucket. Removing a `google_storage_object_acl` sets the
acl to the `private` [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl).

For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls).

-> Want fine-grained control over object ACLs? Use `google_storage_object_access_control` to control individual
role entity pairs.

## Properties

TBC

## See Also

* [google_storage_object_acl](https://www.terraform.io/docs/providers/google/r/storage_object_acl.html) in the _Terraform Provider Documentation_
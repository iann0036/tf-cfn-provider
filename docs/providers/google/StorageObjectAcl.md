# Terraform::Google::StorageObjectAcl

Authoritatively manages the access control list (ACL) for an object in a Google
Cloud Storage (GCS) bucket. Removing a `Terraform::Google::StorageObjectAcl` sets the
acl to the `private` [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl).

For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls).

-> Want fine-grained control over object ACLs? Use `Terraform::Google::StorageObjectAccessControl` to control individual
role entity pairs.

## Properties

`Bucket` - (Required) The name of the bucket the object is stored in.

`Object` - (Required) The name of the object to apply the acl to.

`PredefinedAcl` - (Optional) The "canned" [predefined ACL](https://cloud.google.com/storage/docs/access-control#predefined-acl) to apply. Must be set if `RoleEntity` is not.

`RoleEntity` - (Optional) List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details. Must be set if `PredefinedAcl` is not.


## See Also

* [google_storage_object_acl](https://www.terraform.io/docs/providers/google/r/storage_object_acl.html) in the _Terraform Provider Documentation_
# Terraform::Google::StorageBucket

Creates a new bucket in Google cloud storage service (GCS).
Once a bucket has been created, its location can't be changed.
[ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied
using the [`google_storage_bucket_acl` resource](/docs/providers/google/r/storage_bucket_acl.html).

For more information see
[the official documentation](https://cloud.google.com/storage/docs/overview)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/buckets).

**Note**: When importing a bucket or using only the default provider project for bucket creation, you will need to enable the Compute API and will otherwise get an error with a link to the API enablement page. If you would prefer not to enable the Compute API, make sure to explicitly set `project` on the bucket resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

`Url` - The base URL of the bucket, in the format `gs://<bucket-name>`.

## See Also

* [google_storage_bucket](https://www.terraform.io/docs/providers/google/r/storage_bucket.html) in the _Terraform Provider Documentation_
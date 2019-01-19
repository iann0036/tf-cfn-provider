# Terraform::Google::StorageBucket

Creates a new bucket in Google cloud storage service (GCS).
Once a bucket has been created, its location can't be changed.
[ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied
using the [`Terraform::Google::StorageBucketAcl` resource](/docs/providers/google/r/storage_bucket_acl.html).

For more information see
[the official documentation](https://cloud.google.com/storage/docs/overview)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/buckets).

**Note**: When importing a bucket or using only the default provider project for bucket creation, you will need to enable the Compute API and will otherwise get an error with a link to the API enablement page. If you would prefer not to enable the Compute API, make sure to explicitly set `Project` on the bucket resource.

## Properties

`Name` - (Required) The name of the bucket.

`ForceDestroy` - (Optional, Default: false) When deleting a bucket, this boolean option will delete all contained objects. If you try to delete a bucket that contains objects, Terraform will fail that run.

`Location` - (Optional, Default: 'US') The [GCS location](https://cloud.google.com/storage/docs/bucket-locations).

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`StorageClass` - (Required if action type is `SetStorageClass`) The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`.

`LifecycleRule` - (Optional) The bucket's [Lifecycle Rules](https://cloud.google.com/storage/docs/lifecycle#configuration) configuration. Multiple blocks of this type are permitted. Structure is documented below.

`Versioning` - (Optional) The bucket's [Versioning](https://cloud.google.com/storage/docs/object-versioning) configuration.

`Website` - (Optional) Configuration if the bucket acts as a website. Structure is documented below.

`Cors` - (Optional) The bucket's [Cross-Origin Resource Sharing (CORS)](https://www.w3.org/TR/cors/) configuration. Multiple blocks of this type are permitted. Structure is documented below.

`Labels` - (Optional) A set of key/value label pairs to assign to the bucket.

`Logging` - (Optional) The bucket's [Access & Storage Logs](https://cloud.google.com/storage/docs/access-logs) configuration.

`Encryption` - (Optional) The bucket's encryption configuration.

`RequesterPays` - (Optional, Default: false) Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket.

`Action` - (Required) The Lifecycle Rule's action configuration. A single block of this type is supported. Structure is documented below.

`Condition` - (Required) The Lifecycle Rule's condition configuration. A single block of this type is supported. Structure is documented below.

`Type` - The type of the action of this Lifecycle Rule. Supported values include: `Delete` and `SetStorageClass`.

`Age` - (Optional) Minimum age of an object in days to satisfy this condition.

`CreatedBefore` - (Optional) Creation date of an object in RFC 3339 (e.g. `2017-06-13`) to satisfy this condition.

`IsLive` - (Optional) Defaults to `false` to match archived objects. If `true`, this condition matches live objects. Unversioned buckets have only live objects.

`MatchesStorageClass` - (Optional) [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects to satisfy this condition. Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `STANDARD`, `DURABLE_REDUCED_AVAILABILITY`.

`NumNewerVersions` - (Optional) Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition.

`Enabled` - (Optional) While set to `true`, versioning is fully enabled for this bucket.

`MainPageSuffix` - (Optional) Behaves as the bucket's directory index where missing objects are treated as potential directories.

`NotFoundPage` - (Optional) The custom object to return when a requested resource is not found.

`Origin` - (Optional) The list of [Origins](https://tools.ietf.org/html/rfc6454) eligible to receive CORS response headers. Note: "*" is permitted in the list of origins, and means "any Origin".

`Method` - (Optional) The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".

`ResponseHeader` - (Optional) The list of HTTP headers other than the [simple response headers](https://www.w3.org/TR/cors/#simple-response-header) to give permission for the user-agent to share across domains.

`MaxAgeSeconds` - (Optional) The value, in seconds, to return in the [Access-Control-Max-Age header](https://www.w3.org/TR/cors/#access-control-max-age-response-header) used in preflight responses.

`LogBucket` - (Required) The bucket that will receive log objects.

`LogObjectPrefix` - (Optional, Computed) The object prefix for log objects. If it's not provided, by default GCS sets this to this bucket's name.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

`Url` - The base URL of the bucket, in the format `gs://<bucket-name>`.

## See Also

* [google_storage_bucket](https://www.terraform.io/docs/providers/google/r/storage_bucket.html) in the _Terraform Provider Documentation_
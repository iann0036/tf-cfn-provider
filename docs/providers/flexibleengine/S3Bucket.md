# Terraform::FlexibleEngine::S3Bucket

Provides a S3 bucket resource.

## Properties

`Bucket` - (Optional, Forces new resource) The name of the bucket. If omitted, Terraform will assign a random, unique name.

`BucketPrefix` - (Optional, Forces new resource) Creates a unique bucket name beginning with the specified prefix. Conflicts with `Bucket`.

`Acl` - (Optional) The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

`Policy` - (Optional) A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a `terraform plan`. In this case, please make sure you use the verbose/specific version of the policy.

`ForceDestroy` - (Optional, Default:false ) A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.

`Website` - (Optional) A website object (documented below).

`CorsRule` - (Optional) A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).

`Versioning` - (Optional) A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below).

`Logging` - (Optional) A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).

`LifecycleRule` - (Optional) A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).

`Region` - (Optional) If specified, the region this bucket should reside in. Otherwise, the region used by the callee.

### Website Properties

`IndexDocument` - (Required, unless using `RedirectAllRequestsTo`) Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.

`ErrorDocument` - (Optional) An absolute path to the document to return in case of a 4XX error.

`RedirectAllRequestsTo` - (Optional) A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.

`RoutingRules` - (Optional) A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
describing redirect behavior and when redirects are applied.

### Versioning Properties

`Enabled` - (Optional) Enable versioning. Once you version-enable a bucket, it can never return to an unversioned state. You can, however, suspend versioning on that bucket.

`MfaDelete` - (Optional) Enable MFA delete for either `Change the versioning state of your bucket` or `Permanently delete an object version`. Default is `false`.

### Logging Properties

`TargetBucket` - (Required) The name of the bucket that will receive the log objects.

`TargetPrefix` - (Optional) To specify a key prefix for log objects.

### LifecycleRule Properties

`Id` - (Optional) Unique identifier for the rule.

`Prefix` - (Optional) Object key prefix identifying one or more objects to which the rule applies.

`Enabled` - (Required) Specifies lifecycle rule status.

`Expiration` - (Optional) Specifies a period in the object's expire (documented below).

`NoncurrentVersionExpiration` - (Optional) Specifies when noncurrent object versions expire (documented below).

`Id` - (Optional) Unique identifier for the rule.

`Destination` - (Required) Specifies the destination for the rule (documented below).

`Prefix` - (Required) Object keyname prefix identifying one or more objects to which the rule applies. Set as an empty string to replicate the whole bucket.

`Status` - (Required) The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.

### Destination Properties

`Bucket` - (Required) The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.

`StorageClass` - (Optional) The class of storage used to store the object.


## Return Values

### Fn::GetAtt

`Id` - The name of the bucket.

`Arn` - The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.

`BucketDomainName` - The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.

`HostedZoneId` - The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket's region.

`Region` - The region this bucket resides in.

`WebsiteEndpoint` - The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.

`WebsiteDomain` - The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.

## See Also

* [flexibleengine_s3_bucket](https://www.terraform.io/docs/providers/flexibleengine/r/s3_bucket.html) in the _Terraform Provider Documentation_
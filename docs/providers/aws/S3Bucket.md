# Terraform::AWS::S3Bucket

Provides a S3 bucket resource.

## Properties

`Bucket` - (Required) The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.

`BucketPrefix` - (Optional, Forces new resource) Creates a unique bucket name beginning with the specified prefix. Conflicts with `Bucket`.

`Acl` - (Optional) The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

`Policy` - (Optional) A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a `terraform plan`. In this case, please make sure you use the verbose/specific version of the policy. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`Tags` - (Optional)  A mapping of tags that identifies subset of objects to which the rule applies. The rule applies only to objects having all the tags in its tagset.

`ForceDestroy` - (Optional, Default:false ) A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable.

`Website` - (Optional) A website object (documented below).

`CorsRule` - (Optional) A rule of [Cross-Origin Resource Sharing](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) (documented below).

`Versioning` - (Optional) A state of [versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) (documented below).

`Logging` - (Optional) A settings of [bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/UG/ManagingBucketLogging.html) (documented below).

`LifecycleRule` - (Optional) A configuration of [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) (documented below).

`AccelerationStatus` - (Optional) Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`.

`Region` - (Optional) If specified, the AWS region this bucket should reside in. Otherwise, the region used by the callee.

`RequestPayer` - (Optional) Specifies who should bear the cost of Amazon S3 data transfer. Can be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur the costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html) developer guide for more information.

`ReplicationConfiguration` - (Optional) A configuration of [replication configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html) (documented below).

`ServerSideEncryptionConfiguration` - (Optional) A configuration of [server-side encryption configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) (documented below).

`ObjectLockConfiguration` - (Optional) A configuration of [S3 object locking](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) (documented below).

`IndexDocument` - (Required, unless using `RedirectAllRequestsTo`) Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.

`ErrorDocument` - (Optional) An absolute path to the document to return in case of a 4XX error.

`RedirectAllRequestsTo` - (Optional) A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.

`RoutingRules` - (Optional) A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html) describing redirect behavior and when redirects are applied.

`Enabled` - (Required) Boolean which indicates if this criteria is enabled.

`MfaDelete` - (Optional) Enable MFA delete for either `Change the versioning state of your bucket` or `Permanently delete an object version`. Default is `false`.

`TargetBucket` - (Required) The name of the bucket that will receive the log objects.

`TargetPrefix` - (Optional) To specify a key prefix for log objects.

`Id` - (Optional) Unique identifier for the rule.

`Prefix` - (Optional) Object keyname prefix that identifies subset of objects to which the rule applies.

`Expiration` - (Optional) Specifies a period in the object's expire (documented below).

`Transition` - (Optional) Specifies a period in the object's transitions (documented below).

`NoncurrentVersionExpiration` - (Optional) Specifies when noncurrent object versions expire (documented below).

`NoncurrentVersionTransition` - (Optional) Specifies when noncurrent object versions transitions (documented below).

`Role` - (Required) The ARN of the IAM role for Amazon S3 to assume when replicating the objects.

`Rules` - (Required) Specifies the rules managing the replication (documented below).

`Priority` - (Optional) The priority associated with the rule.

`Destination` - (Required) Specifies the destination for the rule (documented below).

`SourceSelectionCriteria` - (Optional) Specifies special object selection criteria (documented below).

`Status` - (Required) The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.

`Filter` - (Optional) Filter that identifies subset of objects to which the replication rule applies (documented below).

`StorageClass` - (Optional) The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, or `GLACIER`.

`ReplicaKmsKeyId` - (Optional) Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with `SseKmsEncryptedObjects` source selection criteria.

`AccessControlTranslation` - (Optional) Specifies the overrides to use for object owners on replication. Must be used in conjunction with `AccountId` owner override configuration.

`AccountId` - (Optional) The Account ID to use for overriding the object owner on replication. Must be used in conjunction with `AccessControlTranslation` override configuration.

`SseKmsEncryptedObjects` - (Optional) Match SSE-KMS encrypted objects (documented below). If specified, `ReplicaKmsKeyId` in `Destination` must be specified as well.

`Rule` - (Optional) The Object Lock rule in place for this bucket.

`ApplyServerSideEncryptionByDefault` - (required) A single object for setting server-side encryption by default. (documented below).

`SseAlgorithm` - (required) The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`.

`KmsMasterKeyId` - (optional) The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of `SseAlgorithm` as `aws:kms`. The default `aws/s3` AWS KMS master key is used if this element is absent while the `SseAlgorithm` is `aws:kms`.

`Owner` - (Required) The override value for the owner on replicated objects. Currently only `Destination` is supported.

`ObjectLockEnabled` - (Required) Indicates whether this bucket has an Object Lock configuration enabled. Valid value is `Enabled`.

`DefaultRetention` - (Required) The default retention period that you want to apply to new objects placed in this bucket.

`Mode` - (Required) The default Object Lock retention mode you want to apply to new objects placed in this bucket. Valid values are `GOVERNANCE` and `COMPLIANCE`.

`Days` - (Optional) The number of days that you want to specify for the default retention period.

`Years` - (Optional) The number of years that you want to specify for the default retention period.


## Return Values

### Fn::GetAtt

`Id` - The name of the bucket.

`Arn` - The ARN of the bucket. Will be of format `arn:aws:s3:::bucketname`.

`BucketDomainName` - The bucket domain name. Will be of format `bucketname.s3.amazonaws.com`.

`BucketRegionalDomainName` - The bucket region-specific domain name. The bucket domain name including the region name, please refer [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) for format. Note: The AWS CloudFront allows specifying S3 region-specific endpoint when creating S3 origin, it will prevent [redirect issues](https://forums.aws.amazon.com/thread.jspa?threadID=216814) from CloudFront to S3 Origin URL.

`HostedZoneId` - The [Route 53 Hosted Zone ID](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_website_region_endpoints) for this bucket's region.

`Region` - The AWS region this bucket resides in.

`WebsiteEndpoint` - The website endpoint, if the bucket is configured with a website. If not, this will be an empty string.

`WebsiteDomain` - The domain of the website endpoint, if the bucket is configured with a website. If not, this will be an empty string. This is used to create Route 53 alias records.

## See Also

* [aws_s3_bucket](https://www.terraform.io/docs/providers/aws/r/s3_bucket.html) in the _Terraform Provider Documentation_
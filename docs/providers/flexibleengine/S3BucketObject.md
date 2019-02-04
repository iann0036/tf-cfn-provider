# Terraform::FlexibleEngine::S3BucketObject

Provides a S3 bucket object resource.

## Properties

`Bucket` - (Required) The name of the bucket to put the file in.

`Key` - (Required) The name of the object once it is in the bucket.

`Source` - (Required) The path to the source file being uploaded to the bucket.

`Content` - (Required unless `Source` given) The literal content being uploaded to the bucket.

`Acl` - (Optional) The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

`CacheControl` - (Optional) Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.

`ContentDisposition` - (Optional) Specifies presentational information for the object. Read [wc3 content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.

`ContentEncoding` - (Optional) Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.

`ContentLanguage` - (Optional) The language the content is in e.g. en-US or en-GB.

`ContentType` - (Optional) A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.

`WebsiteRedirect` - (Optional) Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).

`Etag` - (Optional) Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`.
This attribute is not compatible with `kms_key_id`.

`ServerSideEncryption` - (Optional) Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".


## Return Values

### Fn::GetAtt

`Id` - the `Key` of the resource supplied above.

`Etag` - the ETag generated for the object (an MD5 sum of the object content).

`VersionId` - A unique version ID value for the object, if bucket versioning.

## See Also

* [flexibleengine_s3_bucket_object](https://www.terraform.io/docs/providers/flexibleengine/r/s3_bucket_object.html) in the _Terraform Provider Documentation_
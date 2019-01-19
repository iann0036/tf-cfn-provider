# Terraform::AWS::S3BucketObject

Provides a S3 bucket object resource.

## Properties

`Bucket` - (Required) The name of the bucket to put the file in.

`Key` - (Required) The name of the object once it is in the bucket.

`Source` - (Required unless `Content` or `ContentBase64` is set) The path to a file that will be read and uploaded as raw bytes for the object content.

`Content` - (Required unless `Source` or `ContentBase64` is set) Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.

`ContentBase64` - (Required unless `Source` or `Content` is set) Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `Source` to stream the content from a disk file.

`Acl` - (Optional) The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to "private".

`CacheControl` - (Optional) Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.

`ContentDisposition` - (Optional) Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.

`ContentEncoding` - (Optional) Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.

`ContentLanguage` - (Optional) The language the content is in e.g. en-US or en-GB.

`ContentType` - (Optional) A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.

`WebsiteRedirect` - (Optional) Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).

`StorageClass` - (Optional) Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) for the object. Can be either "`STANDARD`", "`REDUCED_REDUNDANCY`", "`ONEZONE_IA`", "`INTELLIGENT_TIERING`", "`GLACIER`", or "`STANDARD_IA`". Defaults to "`STANDARD`".

`Etag` - (Optional) Used to trigger updates. The only meaningful value is `${md5(file("path/to/file"))}`. This attribute is not compatible with KMS encryption, `KmsKeyId` or `server_side_encryption = "aws:kms"`.

`ServerSideEncryption` - (Optional) Specifies server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".

`KmsKeyId` - (Optional) Specifies the AWS KMS Key ARN to use for object encryption. This value is a fully qualified **ARN** of the KMS Key. If using `Terraform::AWS::KmsKey`, use the exported `arn` attribute: `kmsKeyId = "${awsKmsKey.foo.arn}"`.

`Tags` - (Optional) A mapping of tags to assign to the object.


## Return Values

### Fn::GetAtt

`Id` - the `Key` of the resource supplied above.

`Etag` - the ETag generated for the object (an MD5 sum of the object content). For plaintext objects or objects encrypted with an AWS-managed key, the hash is an MD5 digest of the object data. For objects encrypted with a KMS key or objects created by either the Multipart Upload or Part Copy operation, the hash is not an MD5 digest, regardless of the method of encryption. More information on possible values can be found on [Common Response Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html).

`VersionId` - A unique version ID value for the object, if bucket versioning.

## See Also

* [aws_s3_bucket_object](https://www.terraform.io/docs/providers/aws/r/s3_bucket_object.html) in the _Terraform Provider Documentation_
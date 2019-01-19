# Terraform::Alicloud::OssBucketObject

Provides a resource to put a object(content or file) to a oss bucket.

## Properties

`Bucket` - (Required) The name of the bucket to put the file in.

`Key` - (Required) The name of the object once it is in the bucket.

`Source` - (Required) The path to the source file being uploaded to the bucket.

`Content` - (Required unless `Source` given) The literal content being uploaded to the bucket.

`Acl` - (Optional) The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".

`ContentType` - (Optional) A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.

`CacheControl` - (Optional) Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.

`ContentDisposition` - (Optional) Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.

`ContentEncoding` - (Optional) Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.

`ContentMd5` - (Optional) The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.

`Expires` - (Optional) Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.

`ServerSideEncryption` - (Optional) Specifies server-side encryption of the object in OSS. At present, it valid value is "`AES256`".


## Return Values

### Fn::GetAtt

`Id` - the `Key` of the resource supplied above.

`ContentLength` - the content length of request.

`Etag` - the ETag generated for the object (an MD5 sum of the object content).

## See Also

* [alicloud_oss_bucket_object](https://www.terraform.io/docs/providers/alicloud/r/oss_bucket_object.html) in the _Terraform Provider Documentation_
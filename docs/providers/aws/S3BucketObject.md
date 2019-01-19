# Terraform::AWS::S3BucketObject

Provides a S3 bucket object resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - the `key` of the resource supplied above.

`Etag` - the ETag generated for the object (an MD5 sum of the object content). For plaintext objects or objects encrypted with an AWS-managed key, the hash is an MD5 digest of the object data. For objects encrypted with a KMS key or objects created by either the Multipart Upload or Part Copy operation, the hash is not an MD5 digest, regardless of the method of encryption. More information on possible values can be found on [Common Response Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html).

`VersionId` - A unique version ID value for the object, if bucket versioning.

## See Also

* [aws_s3_bucket_object](https://www.terraform.io/docs/providers/aws/r/s3_bucket_object.html) in the _Terraform Provider Documentation_
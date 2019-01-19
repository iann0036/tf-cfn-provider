# Terraform::AWS::ElastictranscoderPipeline

Provides an Elastic Transcoder pipeline resource.

## Properties

`AwsKmsKeyArn` - (Optional) The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.

`ContentConfig` - (Optional) The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below).

`ContentConfigPermissions` - (Optional) The permissions for the `ContentConfig` object. (documented below).

`InputBucket` - (Required) The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.

`Name` - (Optional, Forces new resource) The name of the pipeline. Maximum 40 characters.

`Notifications` - (Optional) The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below).

`OutputBucket` - (Optional) The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.

`Role` - (Required) The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.

`ThumbnailConfig` - (Optional) The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below).

`ThumbnailConfigPermissions` - (Optional) The permissions for the `ThumbnailConfig` object. (documented below).

### ContentConfig Properties

`Bucket` - The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.

`StorageClass` - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.

### ContentConfigPermissions Properties

`Access` - The permission that you want to give to the AWS user that you specified in `content_config_permissions.grantee`.

`Grantee` - The AWS user or group that you want to have access to transcoded files and playlists.

`GranteeType` - Specify the type of value that appears in the `content_config_permissions.grantee` object. Valid values are `Canonical`, `Email` or `Group`.

### Notifications Properties

`Completed` - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.

`Error` - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.

`Progressing` - The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.

`Warning` - The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.

### ThumbnailConfig Properties

`Bucket` - The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.

`StorageClass` - The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.

### ThumbnailConfigPermissions Properties

`Access` - The permission that you want to give to the AWS user that you specified in `thumbnail_config_permissions.grantee`.

`Grantee` - The AWS user or group that you want to have access to thumbnail files.

`GranteeType` - Specify the type of value that appears in the `thumbnail_config_permissions.grantee` object.


## See Also

* [aws_elastictranscoder_pipeline](https://www.terraform.io/docs/providers/aws/r/elastictranscoder_pipeline.html) in the _Terraform Provider Documentation_
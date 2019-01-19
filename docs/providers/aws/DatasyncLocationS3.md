# Terraform::AWS::DatasyncLocationS3

Manages an S3 Location within AWS DataSync.

## Properties

`S3BucketArn` - (Required) Amazon Resource Name (ARN) of the S3 Bucket.

`S3Config` - (Required) Configuration block containing information for connecting to S3.

`Subdirectory` - (Required) Prefix to perform actions as source or destination.

`Tags` - (Optional) Key-value pairs of resource tags to assign to the DataSync Location.


## See Also

* [aws_datasync_location_s3](https://www.terraform.io/docs/providers/aws/r/datasync_location_s3.html) in the _Terraform Provider Documentation_
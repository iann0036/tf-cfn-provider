# Terraform::AWS::S3BucketMetric

Provides a S3 bucket [metrics configuration](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html) resource.

## Properties

`Bucket` - (Required) The name of the bucket to put metric configuration.

`Name` - (Required) Unique identifier of the metrics configuration for the bucket.

`Filter` - (Optional) [Object filtering](http://docs.aws.amazon.com/AmazonS3/latest/dev/metrics-configurations.html#metrics-configurations-filter) that accepts a prefix, tags, or a logical AND of prefix and tags (documented below).

### Filter Properties

`Prefix` - (Optional) Object prefix for filtering (singular).

`Tags` - (Optional) Object tags for filtering (up to 10).


## See Also

* [aws_s3_bucket_metric](https://www.terraform.io/docs/providers/aws/r/s3_bucket_metric.html) in the _Terraform Provider Documentation_
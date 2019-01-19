# Terraform::AWS::S3Bucket

Provides a S3 bucket resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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
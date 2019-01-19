# Terraform::AWS::SpotDatafeedSubscription

-> **Note:** There is only a single subscription allowed per account.

To help you understand the charges for your Spot instances, Amazon EC2 provides a data feed that describes your Spot instance usage and pricing.
This data feed is sent to an Amazon S3 bucket that you specify when you subscribe to the data feed.

## Properties

`Bucket` - (Required) The Amazon S3 bucket in which to store the Spot instance data feed.

`Prefix` - (Optional) Path of folder inside bucket to place spot pricing data.


## See Also

* [aws_spot_datafeed_subscription](https://www.terraform.io/docs/providers/aws/r/spot_datafeed_subscription.html) in the _Terraform Provider Documentation_
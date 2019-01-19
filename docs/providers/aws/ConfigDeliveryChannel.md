# Terraform::AWS::ConfigDeliveryChannel

Provides an AWS Config Delivery Channel.

~> **Note:** Delivery Channel requires a [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

## Properties

`Name` - (Optional) The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.

`S3BucketName` - (Required) The name of the S3 bucket used to store the configuration history.

`S3KeyPrefix` - (Optional) The prefix for the specified S3 bucket.

`SnsTopicArn` - (Optional) The ARN of the SNS topic that AWS Config delivers notifications to.

`SnapshotDeliveryProperties` - (Optional) Options for how AWS Config delivers configuration snapshots. See below.


## Return Values

### Fn::GetAtt

`Id` - The name of the delivery channel.

## See Also

* [aws_config_delivery_channel](https://www.terraform.io/docs/providers/aws/r/config_delivery_channel.html) in the _Terraform Provider Documentation_
# Terraform::AWS::KinesisStream

Provides a Kinesis Stream resource. Amazon Kinesis is a managed service that
scales elastically for real-time processing of streaming big data.

For more details, see the [Amazon Kinesis Documentation][1].

## Properties

`Name` - (Required) A name to identify the stream. This is unique to the AWS account and region the Stream is created in.

`RetentionPeriod` - (Optional) Length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours. Minimum value is 24. Default is 24.

`ShardLevelMetrics` - (Optional) A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.

`EncryptionType` - (Optional) The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default value is `NONE`.

`KmsKeyId` - (Optional) The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias aws/kinesis.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The unique Stream id.

`Name` - The unique Stream name.

`ShardCount` - The count of Shards for this Stream.

`Arn` - The Amazon Resource Name (ARN) specifying the Stream (same as `id`).

## See Also

* [aws_kinesis_stream](https://www.terraform.io/docs/providers/aws/r/kinesis_stream.html) in the _Terraform Provider Documentation_
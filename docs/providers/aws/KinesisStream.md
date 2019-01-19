# Terraform::AWS::KinesisStream

Provides a Kinesis Stream resource. Amazon Kinesis is a managed service that
scales elastically for real-time processing of streaming big data.

For more details, see the [Amazon Kinesis Documentation][1].

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The unique Stream id.

`Name` - The unique Stream name.

`ShardCount` - The count of Shards for this Stream.

`Arn` - The Amazon Resource Name (ARN) specifying the Stream (same as `id`).

## See Also

* [aws_kinesis_stream](https://www.terraform.io/docs/providers/aws/r/kinesis_stream.html) in the _Terraform Provider Documentation_
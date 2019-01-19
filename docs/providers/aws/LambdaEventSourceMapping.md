# Terraform::AWS::LambdaEventSourceMapping

Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis, DynamoDB and SQS

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about event source mappings, see [CreateEventSourceMapping][2] in the API docs.

## Properties

`BatchSize` - (Optional) The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB and Kinesis, `10` for SQS.

`EventSourceArn` - (Required) The event source ARN - can either be a Kinesis or DynamoDB stream.

`Enabled` - (Optional) Determines if the mapping will be enabled on creation. Defaults to `true`.

`FunctionName` - (Required) The name or the ARN of the Lambda function that will be subscribing to events.

`StartingPosition` - (Optional) The position in the stream where AWS Lambda should start reading. Must be one of `AT_TIMESTAMP` (Kinesis only), `LATEST` or `TRIM_HORIZON` if getting events from Kinesis or DynamoDB. Must not be provided if getting events from SQS. More information about these positions can be found in the [AWS DynamoDB Streams API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html) and [AWS Kinesis API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType).

`StartingPositionTimestamp` - (Optional) A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of the data record which to start reading when using `StartingPosition` set to `AT_TIMESTAMP`. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.


## Return Values

### Fn::GetAtt

`FunctionArn` - The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `FunctionName` above.).

`LastModified` - The date this resource was last modified.

`LastProcessingResult` - The result of the last AWS Lambda invocation of your Lambda function.

`State` - The state of the event source mapping.

`StateTransitionReason` - The reason the event source mapping is in its current state.

`Uuid` - The UUID of the created event source mapping.

## See Also

* [aws_lambda_event_source_mapping](https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping.html) in the _Terraform Provider Documentation_
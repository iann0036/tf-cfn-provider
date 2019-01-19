# Terraform::AWS::LambdaEventSourceMapping

Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis, DynamoDB and SQS

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about event source mappings, see [CreateEventSourceMapping][2] in the API docs.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`FunctionArn` - The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `function_name` above.).

`LastModified` - The date this resource was last modified.

`LastProcessingResult` - The result of the last AWS Lambda invocation of your Lambda function.

`State` - The state of the event source mapping.

`StateTransitionReason` - The reason the event source mapping is in its current state.

`Uuid` - The UUID of the created event source mapping.

## See Also

* [aws_lambda_event_source_mapping](https://www.terraform.io/docs/providers/aws/r/lambda_event_source_mapping.html) in the _Terraform Provider Documentation_
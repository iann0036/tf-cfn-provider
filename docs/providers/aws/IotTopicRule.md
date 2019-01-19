# Terraform::AWS::IotTopicRule



## Properties

`Name` - (Required) The name of the rule.

`Description` - (Optional) The description of the rule.

`Enabled` - (Required) Specifies whether the rule is enabled.

`Sql` - (Required) The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.

`SqlVersion` - (Required) The version of the SQL rules engine to use when evaluating the rule.

`AlarmName` - (Required) The CloudWatch alarm name.

`RoleArn` - (Required) The ARN of the IAM role that grants access.

`StateReason` - (Required) The reason for the alarm change.

`StateValue` - (Required) The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

`MetricName` - (Required) The CloudWatch metric name.

`MetricNamespace` - (Required) The CloudWatch metric namespace name.

`MetricTimestamp` - (Optional) An optional Unix timestamp (http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).

`MetricUnit` - (Required) The metric unit (supported units can be found here: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit).

`MetricValue` - (Required) The CloudWatch metric value.

`HashKeyField` - (Required) The hash key name.

`HashKeyType` - (Optional) The hash key type. Valid values are "STRING" or "NUMBER".

`HashKeyValue` - (Required) The hash key value.

`PayloadField` - (Optional) The action payload.

`RangeKeyField` - (Optional) The range key name.

`RangeKeyType` - (Optional) The range key type. Valid values are "STRING" or "NUMBER".

`RangeKeyValue` - (Optional) The range key value.

`TableName` - (Required) The name of the DynamoDB table.

`Endpoint` - (Required) The endpoint of your Elasticsearch domain.

`Id` - (Required) The unique identifier for the document you are storing.

`Index` - (Required) The Elasticsearch index where you want to store your data.

`Type` - (Required) The type of document you are storing.

`DeliveryStreamName` - (Required) The delivery stream name.

`Separator` - (Optional) A character separator that is used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).

`PartitionKey` - (Optional) The partition key.

`StreamName` - (Required) The name of the Amazon Kinesis stream.

`FunctionArn` - (Required) The ARN of the Lambda function.

`Topic` - (Required) The name of the MQTT topic the message should be republished to.

`BucketName` - (Required) The Amazon S3 bucket name.

`Key` - (Required) The object key.

`MessageFormat` - (Required) The message format of the message to publish. Accepted values are "JSON" and "RAW".

`TargetArn` - (Required) The ARN of the SNS topic.

`QueueUrl` - (Required) The URL of the Amazon SQS queue.

`UseBase64` - (Required) Specifies whether to use Base64 encoding.


## Return Values

### Fn::GetAtt

`Id` - The name of the topic rule.

`Arn` - The ARN of the topic rule.

## See Also

* [aws_iot_topic_rule](https://www.terraform.io/docs/providers/aws/r/iot_topic_rule.html) in the _Terraform Provider Documentation_
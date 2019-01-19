# Terraform::AWS::SqsQueue



## Properties

`Name` - (Optional) This is the human-readable name of the queue. If omitted, Terraform will assign a random name.

`NamePrefix` - (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`VisibilityTimeoutSeconds` - (Optional) The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).

`MessageRetentionSeconds` - (Optional) The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).

`MaxMessageSize` - (Optional) The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).

`DelaySeconds` - (Optional) The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.

`ReceiveWaitTimeSeconds` - (Optional) The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.

`Policy` - (Optional) The JSON policy for the SQS queue. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`RedrivePolicy` - (Optional) The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).

`FifoQueue` - (Optional) Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.

`ContentBasedDeduplication` - (Optional) Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing).

`KmsMasterKeyId` - (Optional) The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).

`KmsDataKeyReusePeriodSeconds` - (Optional) The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).

`Tags` - (Optional) A mapping of tags to assign to the queue.


## Return Values

### Fn::GetAtt

`Id` - The URL for the created Amazon SQS queue.

`Arn` - The ARN of the SQS queue.

## See Also

* [aws_sqs_queue](https://www.terraform.io/docs/providers/aws/r/sqs_queue.html) in the _Terraform Provider Documentation_
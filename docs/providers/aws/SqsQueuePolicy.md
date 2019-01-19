# Terraform::AWS::SqsQueuePolicy

Allows you to set a policy of an SQS Queue
while referencing ARN of the queue within the policy.

## Properties

`QueueUrl` - (Required) The URL of the SQS Queue to which to attach the policy.

`Policy` - (Required) The JSON policy for the SQS queue. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).


## See Also

* [aws_sqs_queue_policy](https://www.terraform.io/docs/providers/aws/r/sqs_queue_policy.html) in the _Terraform Provider Documentation_
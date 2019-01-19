# Terraform::AWS::SnsTopicSubscription

Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to.
This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests
to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case for Terraform users will
probably be SQS queues.

~> **NOTE:** If the SNS topic and SQS queue are in different AWS regions, it is important for the "aws_sns_topic_subscription" to use an AWS provider that is in the same region of the SNS topic. If the "aws_sns_topic_subscription" is using a provider with a different region than the SNS topic, terraform will fail to create the subscription.

~> **NOTE:** Setup of cross-account subscriptions from SNS topics to SQS queues requires Terraform to have access to BOTH accounts.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts but the same region it is important for the "aws_sns_topic_subscription" to use the AWS provider of the account with the SQS queue. If "aws_sns_topic_subscription" is using a Provider with a different account than the SNS topic, terraform creates the subscriptions but does not keep state and tries to re-create the subscription at every apply.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts and different AWS regions it is important to recognize that the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.

## Properties

`TopicArn` - (Required) The ARN of the SNS topic to subscribe to.

`Protocol` - (Required) The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).

`Endpoint` - (Required) The endpoint to send data to, the contents will vary with the protocol. (see below for more information).

`EndpointAutoConfirms` - (Optional) Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false).

`ConfirmationTimeoutInMinutes` - (Optional) Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

`RawMessageDelivery` - (Optional) Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

`FilterPolicy` - (Optional) JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.

`DeliveryPolicy` - (Optional) JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.


## Return Values

### Fn::GetAtt

`Id` - The ARN of the subscription.

`TopicArn` - The ARN of the topic the subscription belongs to.

`Protocol` - The protocol being used.

`Endpoint` - The full endpoint to send data to (SQS ARN, HTTP(S) URL, Application ARN, SMS number, etc.).

`Arn` - The ARN of the subscription stored as a more user-friendly property.

## See Also

* [aws_sns_topic_subscription](https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription.html) in the _Terraform Provider Documentation_
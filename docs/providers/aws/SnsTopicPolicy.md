# Terraform::AWS::SnsTopicPolicy

Provides an SNS topic policy resource

~> **NOTE:** If a Principal is specified as just an AWS account ID rather than an ARN, AWS silently converts it to the ARN for the root user, causing future terraform plans to differ. To avoid this problem, just specify the full ARN, e.g. `arn:aws:iam::123456789012:root`

## Properties

`Arn` - (Required) The ARN of the SNS topic.

`Policy` - (Required) The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).


## See Also

* [aws_sns_topic_policy](https://www.terraform.io/docs/providers/aws/r/sns_topic_policy.html) in the _Terraform Provider Documentation_
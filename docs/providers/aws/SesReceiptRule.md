# Terraform::AWS::SesReceiptRule

Provides an SES receipt rule resource

## Properties

`Name` - (Required) The name of the rule.

`RuleSetName` - (Required) The name of the rule set.

`After` - (Optional) The name of the rule to place this rule after.

`Enabled` - (Optional) If true, the rule will be enabled.

`Recipients` - (Optional) A list of email addresses.

`ScanEnabled` - (Optional) If true, incoming emails will be scanned for spam and viruses.

`TlsPolicy` - (Optional) Require or Optional.

`AddHeaderAction` - (Optional) A list of Add Header Action blocks. Documented below.

`BounceAction` - (Optional) A list of Bounce Action blocks. Documented below.

`LambdaAction` - (Optional) A list of Lambda Action blocks. Documented below.

`S3Action` - (Optional) A list of S3 Action blocks. Documented below.

`SnsAction` - (Optional) A list of SNS Action blocks. Documented below.

`StopAction` - (Optional) A list of Stop Action blocks. Documented below.

`WorkmailAction` - (Optional) A list of WorkMail Action blocks. Documented below.

`HeaderName` - (Required) The name of the header to add.

`HeaderValue` - (Required) The value of the header to add.

`Position` - (Required) The position of the action in the receipt rule.

`Message` - (Required) The message to send.

`Sender` - (Required) The email address of the sender.

`SmtpReplyCode` - (Required) The RFC 5321 SMTP reply code.

`StatusCode` - (Optional) The RFC 3463 SMTP enhanced status code.

`TopicArn` - (Optional) The ARN of an SNS topic to notify.

`FunctionArn` - (Required) The ARN of the Lambda function to invoke.

`InvocationType` - (Optional) Event or RequestResponse.

`BucketName` - (Required) The name of the S3 bucket.

`KmsKeyArn` - (Optional) The ARN of the KMS key.

`ObjectKeyPrefix` - (Optional) The key prefix of the S3 bucket.

`Scope` - (Required) The scope to apply.

`OrganizationArn` - (Required) The ARN of the WorkMail organization.


## See Also

* [aws_ses_receipt_rule](https://www.terraform.io/docs/providers/aws/r/ses_receipt_rule.html) in the _Terraform Provider Documentation_
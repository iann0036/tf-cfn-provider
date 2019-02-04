# Terraform::AWS::ApiGatewayAccount

Provides a settings of an API Gateway Account. Settings is applied region-wide per `provider` block.

-> **Note:** As there is no API method for deleting account settings or resetting it to defaults, destroying this resource will keep your account settings intact

## Properties

`CloudwatchRoleArn` - (Optional) The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.


## See Also

* [aws_api_gateway_account](https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html) in the _Terraform Provider Documentation_
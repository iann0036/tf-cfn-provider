# Terraform::AWS::LambdaAlias

Creates a Lambda function alias. Creates an alias that points to the specified Lambda function version.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about function aliases, see [CreateAlias][2] and [AliasRoutingConfiguration][3] in the API docs.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) identifying your Lambda function alias.

`InvokeArn` - The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_integration`](/docs/providers/aws/r/api_gateway_integration.html)'s `uri`.

## See Also

* [aws_lambda_alias](https://www.terraform.io/docs/providers/aws/r/lambda_alias.html) in the _Terraform Provider Documentation_
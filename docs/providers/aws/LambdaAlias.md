# Terraform::AWS::LambdaAlias

Creates a Lambda function alias. Creates an alias that points to the specified Lambda function version.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about function aliases, see [CreateAlias][2] and [AliasRoutingConfiguration][3] in the API docs.

## Properties

`Name` - (Required) Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`.

`Description` - (Optional) Description of the alias.

`FunctionName` - (Required) The function ARN of the Lambda function for which you want to create an alias.

`FunctionVersion` - (Required) Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)`.

`RoutingConfig` - (Optional) The Lambda alias' route configuration settings. Fields documented below.

`AdditionalVersionWeights` - (Optional) A map that defines the proportion of events that should be sent to different versions of a lambda function.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) identifying your Lambda function alias.

`InvokeArn` - The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`Terraform::AWS::ApiGatewayIntegration`](/docs/providers/aws/r/apiGatewayIntegration.html)'s `uri`.

## See Also

* [aws_lambda_alias](https://www.terraform.io/docs/providers/aws/r/lambda_alias.html) in the _Terraform Provider Documentation_
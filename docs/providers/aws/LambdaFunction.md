# Terraform::AWS::LambdaFunction

Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS. The Lambda Function itself includes source code and runtime configuration.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) identifying your Lambda Function.

`QualifiedArn` - The Amazon Resource Name (ARN) identifying your Lambda Function Version.

`InvokeArn` - The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_integration`](/docs/providers/aws/r/api_gateway_integration.html)'s `uri`.

`Version` - Latest published version of your Lambda Function.

`LastModified` - The date this resource was last modified.

`KmsKeyArn` - (Optional) The ARN for the KMS encryption key.

`SourceCodeHash` - Base64-encoded representation of raw SHA-256 sum of the zip file, provided either via `filename` or `s3_*` parameters.

`SourceCodeSize` - The size in bytes of the function .zip file.

## See Also

* [aws_lambda_function](https://www.terraform.io/docs/providers/aws/r/lambda_function.html) in the _Terraform Provider Documentation_
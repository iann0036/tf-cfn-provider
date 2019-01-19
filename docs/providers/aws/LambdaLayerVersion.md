# Terraform::AWS::LambdaLayerVersion

Provides a Lambda Layer Version resource. Lambda Layers allow you to reuse shared bits of code across multiple lambda functions.

For information about Lambda Layers and how to use them, see [AWS Lambda Layers][1]

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) identifying your Lambda Layer.

`LayerArn` - The Amazon Resource Name (ARN) identifying your specific Lambda Layer version.

`CreatedDate` - The date this resource was created.

`SourceCodeSize` - The size in bytes of the function .zip file.

`Version` - This Lamba Layer version.

## See Also

* [aws_lambda_layer_version](https://www.terraform.io/docs/providers/aws/r/lambda_layer_version.html) in the _Terraform Provider Documentation_
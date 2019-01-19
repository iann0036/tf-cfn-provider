# Terraform::AWS::LambdaLayerVersion

Provides a Lambda Layer Version resource. Lambda Layers allow you to reuse shared bits of code across multiple lambda functions.

For information about Lambda Layers and how to use them, see [AWS Lambda Layers][1]

## Properties

`S3Bucket` - (Optional) The S3 bucket location containing the function's deployment package. Conflicts with `Filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.

`S3Key` - (Optional) The S3 key of an object containing the function's deployment package. Conflicts with `Filename`.

`S3ObjectVersion` - (Optional) The object version containing the function's deployment package. Conflicts with `Filename`.

`CompatibleRuntimes` - (Optional) A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.

`Description` - (Optional) Description of what your Lambda Layer does.

`LicenseInfo` - (Optional) License info for your Lambda Layer. See [License Info][3].

`SourceCodeHash` - (Optional) Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `Filename` or `S3Key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda layer source archive.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) identifying your Lambda Layer.

`LayerArn` - The Amazon Resource Name (ARN) identifying your specific Lambda Layer version.

`CreatedDate` - The date this resource was created.

`SourceCodeSize` - The size in bytes of the function .zip file.

`Version` - This Lamba Layer version.

## See Also

* [aws_lambda_layer_version](https://www.terraform.io/docs/providers/aws/r/lambda_layer_version.html) in the _Terraform Provider Documentation_
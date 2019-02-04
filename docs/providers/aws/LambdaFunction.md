# Terraform::AWS::LambdaFunction

Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS. The Lambda Function itself includes source code and runtime configuration.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]

## Properties

`Filename` - (Optional) The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.

`S3Bucket` - (Optional) The S3 bucket location containing the function's deployment package. Conflicts with `Filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.

`S3Key` - (Optional) The S3 key of an object containing the function's deployment package. Conflicts with `Filename`.

`S3ObjectVersion` - (Optional) The object version containing the function's deployment package. Conflicts with `Filename`.

`FunctionName` - (Required) A unique name for your Lambda Function.

`DeadLetterConfig` - (Optional) Nested block to configure the function's *dead letter queue*. See details below.

`Handler` - (Required) The function [entrypoint][3] in your code.

`Role` - (Required) IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.

`Description` - (Optional) Description of what your Lambda Function does.

`Layers` - (Optional) List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10].

`MemorySize` - (Optional) Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5].

`Runtime` - (Required) See [Runtimes][6] for valid values.

`Timeout` - (Optional) The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5].

`ReservedConcurrentExecutions` - (Optional) The amount of reserved concurrent executions for this lambda function. Defaults to Unreserved Concurrency Limits. See [Managing Concurrency][9].

`Publish` - (Optional) Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

`VpcConfig` - (Optional) Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7].

`Environment` - (Optional) The Lambda environment's configuration settings. Fields documented below.

`KmsKeyArn` - (Optional) The ARN for the KMS encryption key.

`SourceCodeHash` - (Optional) Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `Filename` or `S3Key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda function source archive.

`Tags` - (Optional) A mapping of tags to assign to the object.

`TargetArn` - (Required) The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function's IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.

`Mode` - (Required) Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
"sampled=1". If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.

`SubnetIds` - (Required) A list of subnet IDs associated with the Lambda function.

`SecurityGroupIds` - (Required) A list of security group IDs associated with the Lambda function.

`Variables` - (Optional) A map that defines environment variables for the Lambda function.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) identifying your Lambda Function.

`QualifiedArn` - The Amazon Resource Name (ARN) identifying your Lambda Function Version.

`InvokeArn` - The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`Terraform::AWS::ApiGatewayIntegration`](/docs/providers/aws/r/apiGatewayIntegration.html)'s `uri`.

`Version` - Latest published version of your Lambda Function.

`LastModified` - The date this resource was last modified.

`KmsKeyArn` - (Optional) The ARN for the KMS encryption key.

`SourceCodeHash` - Base64-encoded representation of raw SHA-256 sum of the zip file, provided either via `Filename` or `s3_*` parameters.

`SourceCodeSize` - The size in bytes of the function .zip file.

## See Also

* [aws_lambda_function](https://www.terraform.io/docs/providers/aws/r/lambda_function.html) in the _Terraform Provider Documentation_
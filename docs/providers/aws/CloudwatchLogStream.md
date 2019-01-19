# Terraform::AWS::CloudwatchLogStream

Provides a CloudWatch Log Stream resource.

## Properties

`Name` - (Required) The name of the log stream. Must not be longer than 512 characters and must not contain `:`.

`LogGroupName` - (Required) The name of the log group under which the log stream is to be created.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) specifying the log stream.

## See Also

* [aws_cloudwatch_log_stream](https://www.terraform.io/docs/providers/aws/r/cloudwatch_log_stream.html) in the _Terraform Provider Documentation_
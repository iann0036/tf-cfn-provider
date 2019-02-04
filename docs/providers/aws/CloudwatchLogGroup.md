# Terraform::AWS::CloudwatchLogGroup

Provides a CloudWatch Log Group resource.

## Properties

`Name` - (Optional, Forces new resource) The name of the log group. If omitted, Terraform will assign a random, unique name.

`NamePrefix` - (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts with `Name`.

`RetentionInDays` - (Optional) Specifies the number of days
you want to retain log events in the specified log group.

`KmsKeyId` - (Optional) The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
permissions for the CMK whenever the encrypted data is requested.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) specifying the log group.

## See Also

* [aws_cloudwatch_log_group](https://www.terraform.io/docs/providers/aws/r/cloudwatch_log_group.html) in the _Terraform Provider Documentation_
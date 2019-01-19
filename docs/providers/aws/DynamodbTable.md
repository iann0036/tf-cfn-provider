# Terraform::AWS::DynamodbTable

Provides a DynamoDB table resource

~> **Note:** It is recommended to use `lifecycle` [`ignore_changes`](/docs/configuration/resources.html#ignore_changes) for `read_capacity` and/or `write_capacity` if there's [autoscaling policy](/docs/providers/aws/r/appautoscaling_policy.html) attached to the table.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Arn` - The arn of the table.

`Id` - The name of the table.

`StreamArn` - The ARN of the Table Stream. Only available when `stream_enabled = true`.

`StreamLabel` - A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not.

## See Also

* [aws_dynamodb_table](https://www.terraform.io/docs/providers/aws/r/dynamodb_table.html) in the _Terraform Provider Documentation_
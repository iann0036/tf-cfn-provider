# Terraform::AWS::DynamodbGlobalTable

Provides a resource to manage a DynamoDB Global Table. These are layered on top of existing DynamoDB Tables.

~> Note: There are many restrictions before you can properly create DynamoDB Global Tables in multiple regions. See the [AWS DynamoDB Global Table Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html) for more information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The name of the DynamoDB Global Table.

`Arn` - The ARN of the DynamoDB Global Table.

## See Also

* [aws_dynamodb_global_table](https://www.terraform.io/docs/providers/aws/r/dynamodb_global_table.html) in the _Terraform Provider Documentation_
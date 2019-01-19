# Terraform::AWS::DynamodbTableItem

Provides a DynamoDB table item resource

-> **Note:** This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.
  You should perform **regular backups** of all data in the table, see [AWS docs for more](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).

## Properties

`TableName` - (Required) The name of the table to contain the item.

`HashKey` - (Required) Hash key to use for lookups and identification of the item.

`RangeKey` - (Optional) Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

`Item` - (Required) JSON representation of a map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.


## See Also

* [aws_dynamodb_table_item](https://www.terraform.io/docs/providers/aws/r/dynamodb_table_item.html) in the _Terraform Provider Documentation_
# Terraform::AWS::DynamodbTable

Provides a DynamoDB table resource

~> **Note:** It is recommended to use `lifecycle` [`ignore_changes`](/docs/configuration/resources.html#ignore_changes) for `ReadCapacity` and/or `WriteCapacity` if there's [autoscaling policy](/docs/providers/aws/r/appautoscaling_policy.html) attached to the table.

## Properties

`Name` - (Required) The name of the table, this needs to be unique
within a region.

`BillingMode` - (Optional) Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.

`HashKey` - (Required, Forces new resource) The attribute to use as the hash (partition) key. Must also be defined as an `Attribute`, see below.

`RangeKey` - (Optional, Forces new resource) The attribute to use as the range (sort) key. Must also be defined as an `Attribute`, see below.

`WriteCapacity` - (Optional) The number of write units for this table. If the `BillingMode` is `PROVISIONED`, this field is required.

`ReadCapacity` - (Optional) The number of read units for this table. If the `BillingMode` is `PROVISIONED`, this field is required.

`Attribute` - (Required) List of nested attribute definitions. Only required for `HashKey` and `RangeKey` attributes. Each attribute has two properties:.

`Name` - (Required) The name of the attribute.

`Type` - (Required) Attribute type, which must be a scalar type: `S`, `N`, or `B` for (S)tring, (N)umber or (B)inary data.

`Ttl` - (Optional) Defines ttl, has two properties, and can only be specified once:.

`Enabled` - (Required) Indicates whether ttl is enabled (true) or disabled (false).

`AttributeName` - (Required) The name of the table attribute to store the TTL timestamp in.

`LocalSecondaryIndex` - (Optional, Forces new resource) Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.

`GlobalSecondaryIndex` - (Optional) Describe a GSO for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.

`StreamEnabled` - (Optional) Indicates whether Streams are to be enabled (true) or disabled (false).

`StreamViewType` - (Optional) When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

`ServerSideEncryption` - (Optional) Encrypt at rest options.

`Tags` - (Optional) A map of tags to populate on the created table.

`PointInTimeRecovery` - (Optional) Point-in-time recovery options.


## Return Values

### Fn::GetAtt

`Arn` - The arn of the table.

`Id` - The name of the table.

`StreamArn` - The ARN of the Table Stream. Only available when `stream_enabled = true`.

`StreamLabel` - A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not.

## See Also

* [aws_dynamodb_table](https://www.terraform.io/docs/providers/aws/r/dynamodb_table.html) in the _Terraform Provider Documentation_
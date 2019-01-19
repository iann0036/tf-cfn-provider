# Terraform::AWS::GlueCatalogTable

Provides a Glue Catalog Table Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality.

## Properties

`Name` - (Required) Name of the table. For Hive compatibility, this must be entirely lowercase.

`DatabaseName` - (Required) Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.

`CatalogId` - (Optional) ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.

`Description` - (Optional) Description of the table.

`Owner` - (Optional) Owner of the table.

`Retention` - (Optional) Retention time for this table.

`StorageDescriptor` - (Optional) A [storage descriptor](#storage_descriptor) object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.

`PartitionKeys` - (Optional) A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

`ViewOriginalText` - (Optional) If the table is a view, the original text of the view; otherwise null.

`ViewExpandedText` - (Optional) If the table is a view, the expanded text of the view; otherwise null.

`TableType` - (Optional) The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).

`Parameters` - (Optional) Properties associated with this table, as a list of key-value pairs.


## See Also

* [aws_glue_catalog_table](https://www.terraform.io/docs/providers/aws/r/glue_catalog_table.html) in the _Terraform Provider Documentation_
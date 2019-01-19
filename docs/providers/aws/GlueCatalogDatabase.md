# Terraform::AWS::GlueCatalogDatabase

Provides a Glue Catalog Database Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality

## Properties

`Name` - (Required) The name of the database.

`CatalogId` - (Optional) ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.

`Description` - (Optional) Description of the database.

`LocationUri` - (Optional) The location of the database (for example, an HDFS path).

`Parameters` - (Optional) A list of key-value pairs that define parameters and properties of the database.


## See Also

* [aws_glue_catalog_database](https://www.terraform.io/docs/providers/aws/r/glue_catalog_database.html) in the _Terraform Provider Documentation_
# Terraform::AWS::DmsEndpoint

Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.

~> **Note:** All arguments including the password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`CertificateArn` - (Optional, Default: empty string) The Amazon Resource Name (ARN) for the certificate.

`DatabaseName` - (Optional) The name of the endpoint database.

`EndpointId` - (Required) The database endpoint identifier.

`EndpointType` - (Required) The type of endpoint. Can be one of `source | target`.

`EngineName` - (Required) The type of engine for the endpoint. Can be one of `mysql | oracle | postgres | mariadb | aurora | redshift | sybase | sqlserver | dynamodb | mongodb | s3 | azuredb`.

`ExtraConnectionAttributes` - (Optional) Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).

`KmsKeyArn` - (Required when `EngineName` is `mongodb`, optional otherwise) The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `KmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.

`Password` - (Optional) The password to be used to login to the endpoint database.

`Port` - (Optional) The port used by the endpoint database.

`ServerName` - (Optional) The host name of the server.

`SslMode` - (Optional, Default: none) The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Username` - (Optional) The user name to be used to login to the endpoint database.

`ServiceAccessRole` - (Optional) The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.

`MongodbSettings` - (Optional) Settings for the source MongoDB endpoint. Available settings are `auth_type` (default: `PASSWORD`), `auth_mechanism` (default: `DEFAULT`), `nesting_level` (default: `NONE`), `extract_doc_id` (default: `false`), `docs_to_investigate` (default: `1000`) and `auth_source` (default: `admin`). For more details, see [Using MongoDB as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html).

`S3Settings` - (Optional) Settings for the target S3 endpoint. Available settings are `service_access_role_arn`, `external_table_definition`, `csv_row_delimiter` (default: `\\n`), `csv_delimiter` (default: `,`), `bucket_folder`, `bucket_name` and `compression_type` (default: `NONE`). For more details, see [Using Amazon S3 as a Target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html).


## Return Values

### Fn::GetAtt

`EndpointArn` - The Amazon Resource Name (ARN) for the endpoint.

## See Also

* [aws_dms_endpoint](https://www.terraform.io/docs/providers/aws/r/dms_endpoint.html) in the _Terraform Provider Documentation_
# Terraform::AWS::KinesisFirehoseDeliveryStream

Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.

For more details, see the [Amazon Kinesis Firehose Documentation][1].

## Properties

`Name` - (Required) A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`KinesisSourceConfiguration` - (Optional) Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.

`S3Configuration` - (Optional) Required for non-S3 destinations. For S3 destination, use `ExtendedS3Configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.

`ExtendedS3Configuration` - (Optional, only Required when `Destination` is `extended_s3`) Enhanced configuration options for the s3 destination. More details are given below.

`RedshiftConfiguration` - (Optional) Configuration options if redshift is the destination.
Using `RedshiftConfiguration` requires the user to also specify a
`S3Configuration` block. More details are given below.

### S3Configuration Properties

`RoleArn` - (Required) The ARN of the AWS credentials.

`BucketArn` - (Required) The ARN of the S3 bucket.

`Prefix` - (Optional) The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket.

`BufferSize` - (Optional) Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.

`BufferInterval` - (Optional) Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.

`CompressionFormat` - (Optional) The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP & Snappy. If the destination is redshift you cannot use ZIP or Snappy.

`KmsKeyArn` - (Optional) Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.

`CloudwatchLoggingOptions` - (Optional) The CloudWatch Logging Options for the delivery stream. More details are given below.

### ExtendedS3Configuration Properties

`DataFormatConversionConfiguration` - (Optional) Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.

`ErrorOutputPrefix` - (Optional) Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.

`ProcessingConfiguration` - (Optional) The data processing configuration.  More details are given below.

`S3BackupMode` - (Optional) The Amazon S3 backup mode.  Valid values are `Disabled` and `Enabled`.  Default value is `Disabled`.

`S3BackupConfiguration` - (Optional) The configuration for backup in Amazon S3. Required if `S3BackupMode` is `Enabled`. Supports the same fields as `S3Configuration` object.

### RedshiftConfiguration Properties

`ClusterJdbcurl` - (Required) The jdbcurl of the redshift cluster.

`Username` - (Required) The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.

`Password` - (Required) The password for the username above.

`RetryDuration` - (Optional) The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.

`RoleArn` - (Required) The arn of the role the stream assumes.

`S3BackupMode` - (Optional) The Amazon S3 backup mode.  Valid values are `Disabled` and `Enabled`.  Default value is `Disabled`.

`S3BackupConfiguration` - (Optional) The configuration for backup in Amazon S3. Required if `S3BackupMode` is `Enabled`. Supports the same fields as `S3Configuration` object.

`DataTableName` - (Required) The name of the table in the redshift cluster that the s3 bucket will copy to.

`CopyOptions` - (Optional) Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the [AWS documentation](http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html).

`DataTableColumns` - (Optional) The data table columns that will be targeted by the copy command.

`CloudwatchLoggingOptions` - (Optional) The CloudWatch Logging Options for the delivery stream. More details are given below.

`ProcessingConfiguration` - (Optional) The data processing configuration.  More details are given below.

`BufferingInterval` - (Optional) Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.

`BufferingSize` - (Optional) Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.

`DomainArn` - (Required) The ARN of the Amazon ES domain.  The IAM role must have permission for `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and `DescribeElasticsearchDomainConfig` after assuming `RoleARN`.  The pattern needs to be `arn:.*`.

`IndexName` - (Required) The Elasticsearch index name.

`IndexRotationPeriod` - (Optional) The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are `NoRotation`, `OneHour`, `OneDay`, `OneWeek`, and `OneMonth`.  The default value is `OneDay`.

`RetryDuration` - (Optional) After an initial failure to deliver to Amazon Elasticsearch, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.

`RoleArn` - (Required) The ARN of the IAM role to be assumed by Firehose for calling the Amazon ES Configuration API and for indexing documents.  The pattern needs to be `arn:.*`.

`S3BackupMode` - (Optional) Defines how documents should be delivered to Amazon S3.  Valid values are `FailedDocumentsOnly` and `AllDocuments`.  Default value is `FailedDocumentsOnly`.

`TypeName` - (Required) The Elasticsearch type name with maximum length of 100 characters.

`CloudwatchLoggingOptions` - (Optional) The CloudWatch Logging Options for the delivery stream. More details are given below.

`ProcessingConfiguration` - (Optional) The data processing configuration.  More details are given below.

`HecAcknowledgmentTimeout` - (Optional) The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.

`HecEndpoint` - (Required) The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.

`HecEndpointType` - (Optional) The HEC endpoint type. Valid values are `Raw` or `Event`. The default value is `Raw`.

`HecToken` - The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.

`S3BackupMode` - (Optional) Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.

`RetryDuration` - (Optional) After an initial failure to deliver to Amazon Elasticsearch, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.

`CloudwatchLoggingOptions` - (Optional) The CloudWatch Logging Options for the delivery stream. More details are given below.

`ProcessingConfiguration` - (Optional) The data processing configuration.  More details are given below.

### CloudwatchLoggingOptions Properties

`Enabled` - (Optional) Enables or disables the logging. Defaults to `false`.

`LogGroupName` - (Optional) The CloudWatch group name for logging. This value is required if `Enabled` is true.

`LogStreamName` - (Optional) The CloudWatch log stream name for logging. This value is required if `Enabled` is true.

### ProcessingConfiguration Properties

`Enabled` - (Optional) Enables or disables data processing.

`Processors` - (Optional) Array of data processors. More details are given below.

### Processors Properties

`Type` - (Required) The type of processor. Valid Values: `Lambda`.

`Parameters` - (Optional) Array of processor parameters. More details are given below.

### Parameters Properties

`ParameterName` - (Required) Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`.

`ParameterValue` - (Required) Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name (ARN) specifying the Stream.

## See Also

* [aws_kinesis_firehose_delivery_stream](https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream.html) in the _Terraform Provider Documentation_
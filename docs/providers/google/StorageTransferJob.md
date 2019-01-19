# Terraform::Google::StorageTransferJob

Creates a new Transfer Job in Google Cloud Storage Transfer.

To get more information about Google Cloud Storage Transfer, see:

* [Overview](https://cloud.google.com/storage-transfer/docs/overview)
* [API documentation](https://cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs#TransferJob)
* How-to Guides
    * [Configuring Access to Data Sources and Sinks](https://cloud.google.com/storage-transfer/docs/configure-access)

## Properties

`Description` - (Required) Unique description to identify the Transfer Job.

`TransferSpec` - (Required) Transfer specification. Structure documented below.

`Schedule` - (Required) Schedule specification defining when the Transfer Job should be scheduled to start, end and and what time to run. Structure documented below.

`Project` - (Optional) The project in which the resource belongs. If it is not provided, the provider project is used.

`Status` - (Optional) Status of the job. Default: `ENABLED`. **NOTE: The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation.**.

### TransferSpec Properties

`GcsDataSink` - (Required) A Google Cloud Storage data sink. Structure documented below.

`ObjectConditions` - (Optional) Only objects that satisfy these object conditions are included in the set of data source and data sink objects. Object conditions based on objects' `last_modification_time` do not exclude objects in a data sink. Structure documented below.

`TransferOptions` - (Optional) Characteristics of how to treat files from datasource and sink during job. If the option `DeleteObjectsUniqueInSink` is true, object conditions based on objects' `last_modification_time` are ignored and do not exclude objects in a data source or a data sink. Structure documented below.

`GcsDataSource` - (Optional) A Google Cloud Storage data source. Structure documented below.

`AwsS3DataSource` - (Optional) An AWS S3 data source. Structure documented below.

`HttpDataSource` - (Optional) An HTTP URL data source. Structure documented below.

### Schedule Properties

`ScheduleStartDate` - (Required) The first day the recurring transfer is scheduled to run. If `ScheduleStartDate` is in the past, the transfer will run for the first time on the following day. Structure documented below.

`ScheduleEndDate` - (Optional) The last day the recurring transfer will be run. If `ScheduleEndDate` is the same as `ScheduleStartDate`, the transfer will be executed only once. Structure documented below.

`StartTimeOfDay` - (Optional) The time in UTC at which the transfer will be scheduled to start in a day. Transfers may start later than this time. If not specified, recurring and one-time transfers that are scheduled to run today will run immediately; recurring transfers that are scheduled to run on a future date will start at approximately midnight UTC on that date. Note that when configuring a transfer with the Cloud Platform Console, the transfer's start time in a day is specified in your local timezone. Structure documented below.

### ObjectConditions Properties

`MaxTimeElapsedSinceLastModification` - (Optional) A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

`MinTimeElapsedSinceLastModification` - (Optional) A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

`IncludePrefixes` - (Optional) If `include_refixes` is specified, objects that satisfy the object conditions must have names that start with one of the `IncludePrefixes` and that do not start with any of the `ExcludePrefixes`. If `IncludePrefixes` is not specified, all objects except those that have names starting with one of the `ExcludePrefixes` must satisfy the object conditions. See [Requirements](https://cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#ObjectConditions).

`ExcludePrefixes` - (Optional) `ExcludePrefixes` must follow the requirements described for `IncludePrefixes`. See [Requirements](https://cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#ObjectConditions).

### TransferOptions Properties

`OverwriteObjectsAlreadyExistingInSink` - (Optional) Whether overwriting objects that already exist in the sink is allowed.

`DeleteObjectsUniqueInSink` - (Optional) Whether objects that exist only in the sink should be deleted. Note that this option and `DeleteObjectsFromSourceAfterTransfer` are mutually exclusive.

`DeleteObjectsFromSourceAfterTransfer` - (Optional) Whether objects should be deleted from the source after they are transferred to the sink. Note that this option and `DeleteObjectsUniqueInSink` are mutually exclusive.

### GcsDataSink Properties

`BucketName` - (Required) Google Cloud Storage bucket name.

### GcsDataSource Properties

`BucketName` - (Required) Google Cloud Storage bucket name.

### AwsS3DataSource Properties

`BucketName` - (Required) S3 Bucket name.

`AwsAccessKey` - (Required) AWS credentials block.

### AwsAccessKey Properties

`AccessKeyId` - (Required) AWS Key ID.

`SecretAccessKey` - (Required) AWS Secret Access Key.

### HttpDataSource Properties

`ListUrl` - (Required) The URL that points to the file that stores the object list entries. This file must allow public access. Currently, only URLs with HTTP and HTTPS schemes are supported.

### ScheduleEndDate Properties

`Year` - (Required) Year of date. Must be from 1 to 9999.

`Month` - (Required) Month of year. Must be from 1 to 12.

`Day` - (Required) Day of month. Must be from 1 to 31 and valid for the year and month.

### ScheduleStartDate Properties

`Hours` - (Required) Hours of day in 24 hour format. Should be from 0 to 23.

`Minutes` - (Required) Minutes of hour of day. Must be from 0 to 59.

`Seconds` - (Optional) Seconds of minutes of the time. Must normally be from 0 to 59.

`Nanos` - (Required) Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.


## Return Values

### Fn::GetAtt

`Name` - The name of the Transfer Job.

`CreationTime` - When the Transfer Job was created.

`LastModificationTime` - When the Transfer Job was last modified.

`DeletionTime` - When the Transfer Job was deleted.

## See Also

* [google_storage_transfer_job](https://www.terraform.io/docs/providers/google/r/storage_transfer_job.html) in the _Terraform Provider Documentation_
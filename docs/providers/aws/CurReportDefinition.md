# Terraform::AWS::CurReportDefinition

Manages Cost and Usage Report Definitions.

~> *NOTE:* The AWS Cost and Usage Report service is only available in `us-east-1` currently.

~> *NOTE:* If AWS Organizations is enabled, only the master account can use this resource.

## Properties

`ReportName` - (Required) Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.

`TimeUnit` - (Required) The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.

`Format` - (Required) Format for report. Valid values are: textORcsv.

`Compression` - (Required) Compression format for report. Valid values are: GZIP, ZIP.

`AdditionalSchemaElements` - (Required) A list of schema elements. Valid values are: RESOURCES.

`S3Bucket` - (Required) Name of the existing S3 bucket to hold generated reports.

`S3Prefix` - (Optional) Report path prefix. Limited to 256 characters.

`S3Region` - (Required) Region of the existing S3 bucket to hold generated reports.

`AdditionalArtifacts` - (Required)  A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.


## See Also

* [aws_cur_report_definition](https://www.terraform.io/docs/providers/aws/r/cur_report_definition.html) in the _Terraform Provider Documentation_
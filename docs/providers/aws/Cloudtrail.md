# Terraform::AWS::Cloudtrail

Provides a CloudTrail resource.

~> *NOTE:* For a multi-region trail, this resource must be in the home region of the trail.

~> *NOTE:* For an organization trail, this resource must be in the master account of the organization.

## Properties

`Name` - (Required) Specifies the name of the trail.

`S3BucketName` - (Required) Specifies the name of the S3 bucket designated for publishing log files.

`S3KeyPrefix` - (Optional) Specifies the S3 key prefix that precedes
the name of the bucket you have designated for log file delivery.

`CloudWatchLogsRoleArn` - (Optional) Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.

`CloudWatchLogsGroupArn` - (Optional) Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.

`EnableLogging` - (Optional) Enables logging for the trail. Defaults to `true`.
Setting this to `false` will pause logging.

`IncludeGlobalServiceEvents` - (Optional) Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to `true`.

`IsMultiRegionTrail` - (Optional) Specifies whether the trail is created in the current
region or in all regions. Defaults to `false`.

`IsOrganizationTrail` - (Optional) Specifies whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to `false`.

`SnsTopicName` - (Optional) Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.

`EnableLogFileValidation` - (Optional) Specifies whether log file integrity validation is enabled.
Defaults to `false`.

`KmsKeyId` - (Optional) Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.

`EventSelector` - (Optional) Specifies an event selector for enabling data event logging. Fields documented below. Please note the [CloudTrail limits](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html) when configuring these.

`Tags` - (Optional) A mapping of tags to assign to the trail.


## See Also

* [aws_cloudtrail](https://www.terraform.io/docs/providers/aws/r/cloudtrail.html) in the _Terraform Provider Documentation_
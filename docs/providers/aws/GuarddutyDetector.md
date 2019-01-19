# Terraform::AWS::GuarddutyDetector

Provides a resource to manage a GuardDuty detector.

~> **NOTE:** Deleting this resource is equivalent to "disabling" GuardDuty for an AWS region, which removes all existing findings. You can set the `Enable` attribute to `false` to instead "suspend" monitoring and feedback reporting while keeping existing data. See the [Suspending or Disabling Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html) for more information.

## Properties

`Enable` - (Optional) Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

`FindingPublishingFrequency` - (Optional) Specifies the frequency of notifications sent for subsequent finding occurrences. Valid values: `FIFTEEN_MINUTES, ONE_HOUR, SIX_HOURS`. Default: `SIX_HOURS`. See [AWS Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_notification_frequency) for more information.


## Return Values

### Fn::GetAtt

`Id` - The ID of the GuardDuty detector.

`AccountId` - The AWS account ID of the GuardDuty detector.

## See Also

* [aws_guardduty_detector](https://www.terraform.io/docs/providers/aws/r/guardduty_detector.html) in the _Terraform Provider Documentation_
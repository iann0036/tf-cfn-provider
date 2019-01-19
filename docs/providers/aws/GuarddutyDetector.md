# Terraform::AWS::GuarddutyDetector

Provides a resource to manage a GuardDuty detector.

~> **NOTE:** Deleting this resource is equivalent to "disabling" GuardDuty for an AWS region, which removes all existing findings. You can set the `enable` attribute to `false` to instead "suspend" monitoring and feedback reporting while keeping existing data. See the [Suspending or Disabling Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html) for more information.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the GuardDuty detector.

`AccountId` - The AWS account ID of the GuardDuty detector.

## See Also

* [aws_guardduty_detector](https://www.terraform.io/docs/providers/aws/r/guardduty_detector.html) in the _Terraform Provider Documentation_
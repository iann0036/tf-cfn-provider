# Terraform::AWS::GuarddutyIpset

Provides a resource to manage a GuardDuty IPSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage IPSets. IPSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html)

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the GuardDuty IPSet.

## See Also

* [aws_guardduty_ipset](https://www.terraform.io/docs/providers/aws/r/guardduty_ipset.html) in the _Terraform Provider Documentation_
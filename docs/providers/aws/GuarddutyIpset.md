# Terraform::AWS::GuarddutyIpset

Provides a resource to manage a GuardDuty IPSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage IPSets. IPSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html)

## Properties

`Activate` - (Required) Specifies whether GuardDuty is to start using the uploaded IPSet.

`DetectorId` - (Required) The detector ID of the GuardDuty.

`Format` - (Required) The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`.

`Location` - (Required) The URI of the file that contains the IPSet.

`Name` - (Required) The friendly name to identify the IPSet.


## Return Values

### Fn::GetAtt

`Id` - The ID of the GuardDuty IPSet.

## See Also

* [aws_guardduty_ipset](https://www.terraform.io/docs/providers/aws/r/guardduty_ipset.html) in the _Terraform Provider Documentation_
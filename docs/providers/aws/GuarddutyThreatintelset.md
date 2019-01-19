# Terraform::AWS::GuarddutyThreatintelset

Provides a resource to manage a GuardDuty ThreatIntelSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html)

## Properties

`Activate` - (Required) Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

`DetectorId` - (Required) The detector ID of the GuardDuty.

`Format` - (Required) The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`.

`Location` - (Required) The URI of the file that contains the ThreatIntelSet.

`Name` - (Required) The friendly name to identify the ThreatIntelSet.


## Return Values

### Fn::GetAtt

`Id` - The ID of the GuardDuty ThreatIntelSet and the detector ID. Format: `<DetectorID>:<ThreatIntelSetID>`.

## See Also

* [aws_guardduty_threatintelset](https://www.terraform.io/docs/providers/aws/r/guardduty_threatintelset.html) in the _Terraform Provider Documentation_
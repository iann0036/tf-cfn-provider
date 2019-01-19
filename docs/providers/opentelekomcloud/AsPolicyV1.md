# Terraform::OpenTelekomCloud::AsPolicyV1

Manages a V1 AS Policy resource within OpenTelekomCloud.

## Properties

`Region` - (Optional) The region in which to create the AS policy. If omitted, the `Region` argument of the provider is used. Changing this creates a new AS policy.

`ScalingPolicyName` - (Required) The name of the AS policy. The name can contain letters, digits, underscores(_), and hyphens(-),and cannot exceed 64 characters.

`ScalingGroupId` - (Required) The AS group ID. Changing this creates a new AS policy.

`ScalingPolicyType` - (Required) The AS policy type. The values can be `ALARM`, `SCHEDULED`, and `RECURRENCE`.

`AlarmId` - (Optional) The alarm rule ID. This argument is mandatory when `ScalingPolicyType` is set to `ALARM`.

`ScheduledPolicy` - (Optional) The periodic or scheduled AS policy. This argument is mandatory when `ScalingPolicyType` is set to `SCHEDULED` or `RECURRENCE`. The scheduled_policy structure is documented below.

`ScalingPolicyAction` - (Optional) The action of the AS policy. The scaling_policy_action structure is documented below.

`CoolDownTime` - (Optional) The cooling duration (in seconds), and is 900 by default.

`LaunchTime` - (Required) The time when the scaling action is triggered. If `ScalingPolicyType` is set to `SCHEDULED`, the time format is YYYY-MM-DDThh:mmZ. If `ScalingPolicyType` is set to `RECURRENCE`, the time format is hh:mm.

`RecurrenceType` - (Optional) The periodic triggering type. This argument is mandatory when `ScalingPolicyType` is set to `RECURRENCE`. The options include `Daily`, `Weekly`, and `Monthly`.

`RecurrenceValue` - (Optional) The frequency at which scaling actions are triggered.

`StartTime` - (Optional) The start time of the scaling action triggered periodically. The time format complies with UTC. The current time is used by default. The time format is YYYY-MM-DDThh:mmZ.

`EndTime` - (Optional) The end time of the scaling action triggered periodically. The time format complies with UTC. This argument is mandatory when `ScalingPolicyType` is set to `RECURRENCE`. The time format is YYYY-MM-DDThh:mmZ.

`Operation` - (Optional) The operation to be performed. The options include `ADD` (default), `REMOVE`, and `SET`.

`InstanceNumber` - (Optional) The number of instances to be operated. The default number is 1.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`ScalingPolicyName` - See Properties above.

`ScalingPolicyType` - See Properties above.

`AlarmId` - See Properties above.

`CoolDownTime` - See Properties above.

`ScalingPolicyAction/operation` - See Properties above.

`ScalingPolicyAction/instanceNumber` - See Properties above.

`ScheduledPolicy/launchTime` - See Properties above.

`ScheduledPolicy/recurrenceType` - See Properties above.

`ScheduledPolicy/recurrenceValue` - See Properties above.

`ScheduledPolicy/startTime` - See Properties above.

`ScheduledPolicy/endTime` - See Properties above.

## See Also

* [opentelekomcloud_as_policy_v1](https://www.terraform.io/docs/providers/opentelekomcloud/r/as_policy_v1.html) in the _Terraform Provider Documentation_
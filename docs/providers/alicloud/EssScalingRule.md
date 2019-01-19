# Terraform::Alicloud::EssScalingRule

Provides a ESS scaling rule resource.

## Properties

`ScalingGroupId` - (Required) ID of the scaling group of a scaling rule.

`AdjustmentType` - (Required) Adjustment mode of a scaling rule. Optional values: - QuantityChangeInCapacity: It is used to increase or decrease a specified number of ECS instances. - PercentChangeInCapacity: It is used to increase or decrease a specified proportion of ECS instances. - TotalCapacity: It is used to adjust the quantity of ECS instances in the current scaling group to a specified value.

`AdjustmentValue` - (Required) Adjusted value of a scaling rule. Value range: - QuantityChangeInCapacity：(0, 100] U (-100, 0] - PercentChangeInCapacity：[0, 10000] U [-10000, 0] - TotalCapacity：[0, 100].

`ScalingRuleName` - (Optional) Name shown for the scaling rule, which is a string containing 2 to 40 English or Chinese characters.

`Cooldown` - (Optional) Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The default value is empty.


## Return Values

### Fn::GetAtt

`Id` - The scaling rule ID.

`ScalingGroupId` - The id of scaling group.

`Ari` - Unique identifier of a scaling rule.

`AdjustmentType` - Adjustment mode of a scaling rule.

`AdjustmentValue` - Adjustment value of a scaling rule.

`ScalingRuleName` - Name of a scaling rule.

`Cooldown` - Cool-down time of a scaling rule.

## See Also

* [alicloud_ess_scaling_rule](https://www.terraform.io/docs/providers/alicloud/r/ess_scaling_rule.html) in the _Terraform Provider Documentation_
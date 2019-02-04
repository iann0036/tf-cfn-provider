# Terraform::NewRelic::AlertPolicy



## Properties

`Name` - (Required) The name of the policy.
* `IncidentPreference` - (Optional) The rollup strategy for the policy.  Options include: `PER_POLICY`, `PER_CONDITION`, or `PER_CONDITION_AND_TARGET`.  The default is `PER_POLICY`.

`IncidentPreference` - (Optional) The rollup strategy for the policy.  Options include: `PER_POLICY`, `PER_CONDITION`, or `PER_CONDITION_AND_TARGET`.  The default is `PER_POLICY`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

`CreatedAt` - The time the policy was created.

`UpdatedAt` - The time the policy was last updated.

## See Also

* [newrelic_alert_policy](https://www.terraform.io/docs/providers/newrelic/r/alert_policy.html) in the _Terraform Provider Documentation_
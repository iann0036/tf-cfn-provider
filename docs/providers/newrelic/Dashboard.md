# Terraform::NewRelic::Dashboard



## Properties

`Title` - (Required) The title of the dashboard.
* `Icon` - (Optional) The icon for the dashboard.  Defaults to `bar-chart`.
* `Visibility` - (Optional) Who can see the dashboard in an account. Must be `owner` or `all`. Defaults to `all`.
* `Widget` - (Optional) A widget that describes a visualization. See [Widgets](#widgets) below for details.
* `Editable` - (Optional) Who can edit the dashboard in an account. Must be `read_only`, `editable_by_owner`, `editable_by_all`, or `all`. Defaults to `editable_by_all`.

`Icon` - (Optional) The icon for the dashboard.  Defaults to `bar-chart`.
* `Visibility` - (Optional) Who can see the dashboard in an account. Must be `owner` or `all`. Defaults to `all`.
* `Widget` - (Optional) A widget that describes a visualization. See [Widgets](#widgets) below for details.
* `Editable` - (Optional) Who can edit the dashboard in an account. Must be `read_only`, `editable_by_owner`, `editable_by_all`, or `all`. Defaults to `editable_by_all`.

`Visibility` - (Optional) Who can see the dashboard in an account. Must be `owner` or `all`. Defaults to `all`.
* `Widget` - (Optional) A widget that describes a visualization. See [Widgets](#widgets) below for details.
* `Editable` - (Optional) Who can edit the dashboard in an account. Must be `read_only`, `editable_by_owner`, `editable_by_all`, or `all`. Defaults to `editable_by_all`.

`Widget` - (Optional) A widget that describes a visualization. See [Widgets](#widgets) below for details.
* `Editable` - (Optional) Who can edit the dashboard in an account. Must be `read_only`, `editable_by_owner`, `editable_by_all`, or `all`. Defaults to `editable_by_all`.

`Editable` - (Optional) Who can edit the dashboard in an account. Must be `read_only`, `editable_by_owner`, `editable_by_all`, or `all`. Defaults to `editable_by_all`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the dashboard.

## See Also

* [newrelic_dashboard](https://www.terraform.io/docs/providers/newrelic/r/dashboard.html) in the _Terraform Provider Documentation_
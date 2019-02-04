# Terraform::PagerDuty::Addon

With [add-ons](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Add-ons/get_addons), third-party developers can write their own add-ons to PagerDuty's UI. Given a configuration containing a src parameter, that URL will be embedded in an iframe on a page that's available to users from a drop-down menu.

## Properties

`Name` - (Required) The name of the add-on.

`Src` - (Required) The source URL to display in a frame in the PagerDuty UI. `HTTPS` is required.


## Return Values

### Fn::GetAtt

`Id` - The ID of the add-on.

## See Also

* [pagerduty_addon](https://www.terraform.io/docs/providers/pagerduty/r/addon.html) in the _Terraform Provider Documentation_
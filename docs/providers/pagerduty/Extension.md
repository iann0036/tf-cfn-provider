# Terraform::PagerDuty::Extension

An [extension](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Extensions/post_extensions) can be associated with a service.

## Properties

`Name` - (Optional) The name of the service extension.

`EndpointUrl` - (Optional) The url of the extension.

`ExtensionSchema` - (Required) This is the schema for this extension.

`ExtensionObjects` - (Required) This is the objects for which the extension applies (An array of service ids).

`Config` - (Optional) The configuration of the service extension as string containing plain JSON-encoded data.


## Return Values

### Fn::GetAtt

`Id` - The ID of the extension.

`HtmlUrl` - a URL at which the entity is uniquely displayed in the Web app.

## See Also

* [pagerduty_extension](https://www.terraform.io/docs/providers/pagerduty/r/extension.html) in the _Terraform Provider Documentation_
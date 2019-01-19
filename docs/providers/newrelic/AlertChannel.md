# Terraform::NewRelic::AlertChannel



## Properties

`Name` - (Required) The name of the channel. * `Type` - (Required) The type of channel.  One of: `campfire`, `email`, `hipchat`, `opsgenie`, `pagerduty`, `slack`, `victorops`, or `webhook`. * `Configuration` - (Required) A map of key / value pairs with channel type specific values.

`Type` - (Required) The type of channel.  One of: `campfire`, `email`, `hipchat`, `opsgenie`, `pagerduty`, `slack`, `victorops`, or `webhook`. * `Configuration` - (Required) A map of key / value pairs with channel type specific values.

`Configuration` - (Required) A map of key / value pairs with channel type specific values.


## Return Values

### Fn::GetAtt

`Id` - The ID of the channel.

## See Also

* [newrelic_alert_channel](https://www.terraform.io/docs/providers/newrelic/r/alert_channel.html) in the _Terraform Provider Documentation_
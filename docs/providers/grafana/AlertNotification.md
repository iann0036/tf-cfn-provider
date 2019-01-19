# Terraform::Grafana::AlertNotification

The alert notification resource allows an alert notification channel to be created on a Grafana server.

## Properties

`Name` - (Required) The name of the alert notification channel.

`Type` - (Required) The type of the alert notification channel.

`IsDefault` - (Optional) Is this the default channel for all your alerts.

`Settings` - (Optional) Additional settings, for full reference lookup [Grafana HTTP API documentation](http://docs.grafana.org/http_api/alerting).


## Return Values

### Fn::GetAtt

`Id` - The ID of the resource.

## See Also

* [grafana_alert_notification](https://www.terraform.io/docs/providers/grafana/r/alert_notification.html) in the _Terraform Provider Documentation_
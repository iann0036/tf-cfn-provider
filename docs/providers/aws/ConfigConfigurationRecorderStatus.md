# Terraform::AWS::ConfigConfigurationRecorderStatus

Manages status (recording / stopped) of an AWS Config Configuration Recorder.

~> **Note:** Starting Configuration Recorder requires a [Delivery Channel](/docs/providers/aws/r/config_delivery_channel.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

## Properties

`Name` - (Required) The name of the recorder.

`IsEnabled` - (Required) Whether the configuration recorder should be enabled or disabled.


## See Also

* [aws_config_configuration_recorder_status](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder_status.html) in the _Terraform Provider Documentation_
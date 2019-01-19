# Terraform::AWS::ConfigConfigurationRecorderStatus

Manages status (recording / stopped) of an AWS Config Configuration Recorder.

~> **Note:** Starting Configuration Recorder requires a [Delivery Channel](/docs/providers/aws/r/config_delivery_channel.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [aws_config_configuration_recorder_status](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder_status.html) in the _Terraform Provider Documentation_
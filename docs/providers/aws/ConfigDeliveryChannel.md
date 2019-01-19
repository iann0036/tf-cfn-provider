# Terraform::AWS::ConfigDeliveryChannel

Provides an AWS Config Delivery Channel.

~> **Note:** Delivery Channel requires a [Configuration Recorder](/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The name of the delivery channel.

## See Also

* [aws_config_delivery_channel](https://www.terraform.io/docs/providers/aws/r/config_delivery_channel.html) in the _Terraform Provider Documentation_
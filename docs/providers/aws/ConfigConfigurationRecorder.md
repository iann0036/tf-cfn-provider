# Terraform::AWS::ConfigConfigurationRecorder

Provides an AWS Config Configuration Recorder. Please note that this resource **does not start** the created recorder automatically.

~> **Note:** _Starting_ the Configuration Recorder requires a [delivery channel](/docs/providers/aws/r/config_delivery_channel.html) (while delivery channel creation requires Configuration Recorder). This is why [`Terraform::AWS::ConfigConfigurationRecorderStatus`](/docs/providers/aws/r/config_configuration_recorder_status.html) is a separate resource.

## Properties

`Name` - (Optional) The name of the recorder. Defaults to `default`. Changing it recreates the resource.

`RoleArn` - (Required) Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

`RecordingGroup` - (Optional) Recording group - see below.


## Return Values

### Fn::GetAtt

`Id` - Name of the recorder.

## See Also

* [aws_config_configuration_recorder](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html) in the _Terraform Provider Documentation_
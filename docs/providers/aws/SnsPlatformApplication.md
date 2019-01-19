# Terraform::AWS::SnsPlatformApplication

Provides an SNS platform application resource

## Properties

`Name` - (Required) The friendly name for the SNS platform application.

`Platform` - (Required) The platform that the app is registered with. See [Platform][1] for supported platforms.

`PlatformCredential` - (Required) Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

`EventDeliveryFailureTopicArn` - (Optional) SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

`EventEndpointCreatedTopicArn` - (Optional) SNS Topic triggered when a new platform endpoint is added to your platform application.

`EventEndpointDeletedTopicArn` - (Optional) SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

`EventEndpointUpdatedTopicArn` - (Optional) SNS Topic triggered when an existing platform endpoint is changed from your platform application.

`FailureFeedbackRoleArn` - (Optional) The IAM role permitted to receive failure feedback for this application.

`PlatformPrincipal` - (Optional) Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

`SuccessFeedbackRoleArn` - (Optional) The IAM role permitted to receive success feedback for this application.

`SuccessFeedbackSampleRate` - (Optional) The percentage of success to sample (0-100).


## Return Values

### Fn::GetAtt

`Id` - The ARN of the SNS platform application.

`Arn` - The ARN of the SNS platform application.

## See Also

* [aws_sns_platform_application](https://www.terraform.io/docs/providers/aws/r/sns_platform_application.html) in the _Terraform Provider Documentation_
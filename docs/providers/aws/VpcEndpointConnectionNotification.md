# Terraform::AWS::VpcEndpointConnectionNotification

Provides a VPC Endpoint connection notification resource.
Connection notifications notify subscribers of VPC Endpoint events.

## Properties

`VpcEndpointServiceId` - (Optional) The ID of the VPC Endpoint Service to receive notifications for.

`VpcEndpointId` - (Optional) The ID of the VPC Endpoint to receive notifications for.

`ConnectionNotificationArn` - (Required) The ARN of the SNS topic for the notifications.

`ConnectionEvents` - (Required) One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPC connection notification.

`State` - The state of the notification.

`NotificationType` - The type of notification.

## See Also

* [aws_vpc_endpoint_connection_notification](https://www.terraform.io/docs/providers/aws/r/vpc_endpoint_connection_notification.html) in the _Terraform Provider Documentation_
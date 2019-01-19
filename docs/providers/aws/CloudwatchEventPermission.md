# Terraform::AWS::CloudwatchEventPermission

Provides a resource to create a CloudWatch Events permission to support cross-account events in the current account default event bus.

## Properties

`Principal` - (Required) The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus, optionally limited by `Condition`.

`StatementId` - (Required) An identifier string for the external account that you are granting permissions to.

`Action` - (Optional) The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.

`Condition` - (Optional) Configuration block to limit the event bus permissions you are granting to only accounts that fulfill the condition. Specified below.


## Return Values

### Fn::GetAtt

`Id` - The statement ID of the CloudWatch Events permission.

## See Also

* [aws_cloudwatch_event_permission](https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_permission.html) in the _Terraform Provider Documentation_
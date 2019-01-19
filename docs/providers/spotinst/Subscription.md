# Terraform::Spotinst::Subscription

Provides a Spotinst subscription resource.

## Properties

`ResourceId` - (Required) Spotinst Resource ID (Elastigroup ID).

`EventType` - (Required) The event to send the notification when triggered. Valid values: `"AWS_EC2_INSTANCE_TERMINATE"`, `"AWS_EC2_INSTANCE_TERMINATED"`, `"AWS_EC2_INSTANCE_LAUNCH"`, `"AWS_EC2_INSTANCE_UNHEALTHY_IN_ELB"`, `"GROUP_ROLL_FAILED"`, `"GROUP_ROLL_FINISHED"`, `"CANT_SCALE_UP_GROUP_MAX_CAPACITY"`, `"GROUP_UPDATED"`, `"AWS_EC2_CANT_SPIN_OD"`, `"AWS_EMR_PROVISION_TIMEOUT"`, `"AWS_EC2_INSTANCE_READY_SIGNAL_TIMEOUT"`.

`Protocol` - (Required) The protocol to send the notification. Valid values: `"http"`, `"https"`, `"email"`, `"email-json"`, `"aws-sns"`, `"web"`.

`Endpoint` - (Required) The endpoint the notification will be sent to: url in case of `"http"`/`"https"`, email address in case of `"email"`/`"email-json"`, sns-topic-arn in case of `"aws-sns"`.

`Format` - (Optional) The format of the notification content (JSON Format - Key+Value). Valid values: `"%instance-id%"`, `"%event%"`, `"%resource-id%"`, `"%resource-name%"`.


## Return Values

### Fn::GetAtt

`Id` - The subscription ID.

## See Also

* [spotinst_subscription](https://www.terraform.io/docs/providers/spotinst/r/subscription.html) in the _Terraform Provider Documentation_
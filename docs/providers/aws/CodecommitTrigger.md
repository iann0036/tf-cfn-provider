# Terraform::AWS::CodecommitTrigger

Provides a CodeCommit Trigger Resource.

~> **NOTE on CodeCommit**: The CodeCommit is not yet rolled out
in all regions - available regions are listed
[the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region).

## Properties

`RepositoryName` - (Required) The name for the repository. This needs to be less than 100 characters.

`Name` - (Required) The name of the trigger.

`DestinationArn` - (Required) The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).

`CustomData` - (Optional) Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.

`Branches` - (Optional) The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.

`Events` - (Required) The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: `all`, `updateReference`, `createReference`, `deleteReference`.


## See Also

* [aws_codecommit_trigger](https://www.terraform.io/docs/providers/aws/r/codecommit_trigger.html) in the _Terraform Provider Documentation_
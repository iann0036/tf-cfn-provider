# Terraform::AWS::SsmAssociation

Associates an SSM Document to an instance or EC2 tag.

## Properties

`Name` - (Required) The name of the SSM document to apply.

`AssociationName` - (Optional) The descriptive name for the association.

`DocumentVersion` - (Optional) The document version you want to associate with the target(s). Can be a specific version or the default version.

`InstanceId` - (Optional) The instance ID to apply an SSM document to. Use `Targets` with key `InstanceIds` for document schema versions 2.0 and above.

`OutputLocation` - (Optional) An output location block. Output Location is documented below.

`Parameters` - (Optional) A block of arbitrary string parameters to pass to the SSM document.

`ScheduleExpression` - (Optional) A cron expression when the association will be applied to the target(s).

`Targets` - (Optional) A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.

`S3BucketName` - (Required) The S3 bucket name.

`S3KeyPrefix` - (Optional) The S3 bucket prefix. Results stored in the root if not configured.

`Key` - (Required) Either `InstanceIds` or `tag:Tag Name` to specify an EC2 tag.

`Values` - (Required) A list of instance IDs or tag values. AWS currently limits this to 1 target value.


## Return Values

### Fn::GetAtt

`Name` - The name of the SSM document to apply.

`InstanceIds` - The instance id that the SSM document was applied to.

`Parameters` - Additional parameters passed to the SSM document.

## See Also

* [aws_ssm_association](https://www.terraform.io/docs/providers/aws/r/ssm_association.html) in the _Terraform Provider Documentation_
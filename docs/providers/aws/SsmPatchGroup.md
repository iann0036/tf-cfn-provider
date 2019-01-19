# Terraform::AWS::SsmPatchGroup

Provides an SSM Patch Group resource

## Properties

`BaselineId` - (Required) The ID of the patch baseline to register the patch group with.

`PatchGroup` - (Required) The name of the patch group that should be registered with the patch baseline.


## Return Values

### Fn::GetAtt

`Id` - The ID of the patch baseline.

## See Also

* [aws_ssm_patch_group](https://www.terraform.io/docs/providers/aws/r/ssm_patch_group.html) in the _Terraform Provider Documentation_
# Terraform::AWS::SsmPatchBaseline

Provides an SSM Patch Baseline resource

~> **NOTE on Patch Baselines:** The `approved_patches` and `approval_rule` are 
both marked as optional fields, but the Patch Baseline requires that at least one
of them is specified.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the patch baseline.

## See Also

* [aws_ssm_patch_baseline](https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline.html) in the _Terraform Provider Documentation_
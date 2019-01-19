# Terraform::AWS::SsmPatchBaseline

Provides an SSM Patch Baseline resource

~> **NOTE on Patch Baselines:** The `ApprovedPatches` and `ApprovalRule` are 
both marked as optional fields, but the Patch Baseline requires that at least one
of them is specified.

## Properties

`Name` - (Required) The name of the patch baseline.

`Description` - (Optional) The description of the patch baseline.

`OperatingSystem` - (Optional) Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.

`ApprovedPatchesComplianceLevel` - (Optional) Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

`ApprovedPatches` - (Optional) A list of explicitly approved patches for the baseline.

`RejectedPatches` - (Optional) A list of rejected patches.

`GlobalFilter` - (Optional) A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.

`ApprovalRule` - (Optional) A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.

### ApprovalRule Properties

`ApproveAfterDays` - (Required) The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100.

`PatchFilter` - (Required) The patch filter group that defines the criteria for the rule. Up to 4 patch filters can be specified per approval rule using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.

`ComplianceLevel` - (Optional) Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

`EnableNonSecurity` - (Optional) Boolean enabling the application of non-security updates. The default value is 'false'. Valid for Linux instances only.


## Return Values

### Fn::GetAtt

`Id` - The ID of the patch baseline.

## See Also

* [aws_ssm_patch_baseline](https://www.terraform.io/docs/providers/aws/r/ssm_patch_baseline.html) in the _Terraform Provider Documentation_
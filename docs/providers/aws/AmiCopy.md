# Terraform::AWS::AmiCopy

The "AMI copy" resource allows duplication of an Amazon Machine Image (AMI),
including cross-region copies.

If the source AMI has associated EBS snapshots, those will also be duplicated
along with the AMI.

This is useful for taking a single AMI provisioned in one region and making
it available in another for a multi-region deployment.

Copying an AMI can take several minutes. The creation of this resource will
block until the new AMI is available for use on new instances.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the created AMI.

## See Also

* [aws_ami_copy](https://www.terraform.io/docs/providers/aws/r/ami_copy.html) in the _Terraform Provider Documentation_
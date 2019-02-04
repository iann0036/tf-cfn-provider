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

`Name` - (Required) A region-unique name for the AMI.

`SourceAmiId` - (Required) The id of the AMI to copy. This id must be valid in the region
given by `SourceAmiRegion`.

`SourceAmiRegion` - (Required) The region from which the AMI will be copied. This may be the
same as the AWS provider region in order to create a copy within the same region.

`Encrypted` - (Optional) Specifies whether the destination snapshots of the copied image should be encrypted. Defaults to `false`.

`KmsKeyId` - (Optional) The full ARN of the KMS Key to use when encrypting the snapshots of an image during a copy operation. If not specified, then the default AWS KMS Key will be used.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the created AMI.

## See Also

* [aws_ami_copy](https://www.terraform.io/docs/providers/aws/r/ami_copy.html) in the _Terraform Provider Documentation_
# Terraform::AWS::SagemakerNotebookInstance

Provides a Sagemaker Notebook Instance resource.

## Properties

`Name` - (Required) The name of the notebook instance (must be unique).

`RoleArn` - (Required) The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.

`InstanceType` - (Required) The name of ML compute instance type.

`SubnetId` - (Optional) The VPC subnet ID.

`SecurityGroups` - (Optional) The associated security groups.

`KmsKeyId` - (Optional) The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The name of the notebook instance.

`Arn` - The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.

## See Also

* [aws_sagemaker_notebook_instance](https://www.terraform.io/docs/providers/aws/r/sagemaker_notebook_instance.html) in the _Terraform Provider Documentation_
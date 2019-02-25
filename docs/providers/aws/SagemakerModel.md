# Terraform::AWS::SagemakerModel

Provides a SageMaker model resource.

## Properties

`Name` - (Optional) The name of the model (must be unique). If omitted, Terraform will assign a random, unique name.

`PrimaryContainer` - (Optional) The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `Container` argument is required. Fields are documented below.

`ExecutionRoleArn` - (Required) A role that SageMaker can assume to access model artifacts and docker images for deployment.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Container Properties

`Image` - (Required) The registry path where the inference code image is stored in Amazon ECR.

`ModelDataUrl` - (Optional) The URL for the S3 location where model artifacts are stored.

`ContainerHostname` - (Optional) The DNS host name for the container.

`Environment` - (Optional) Environment variables for the Docker container.
A list of key value pairs.


## Return Values

### Fn::GetAtt

`Name` - The name of the model.

`Arn` - The Amazon Resource Name (ARN) assigned by AWS to this model.

## See Also

* [aws_sagemaker_model](https://www.terraform.io/docs/providers/aws/r/sagemaker_model.html) in the _Terraform Provider Documentation_
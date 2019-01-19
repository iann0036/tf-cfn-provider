# Terraform::AWS::DevicefarmProject

Provides a resource to manage AWS Device Farm Projects. 
Please keep in mind that this feature is only supported on the "us-west-2" region.
This resource will error if you try to create a project in another region.

For more information about Device Farm Projects, see the AWS Documentation on
[Device Farm Projects][aws-get-project].

## Properties

`Name` - (Required) The name of the project.


## Return Values

### Fn::GetAtt

`Arn` - The Amazon Resource Name of this project.

## See Also

* [aws_devicefarm_project](https://www.terraform.io/docs/providers/aws/r/devicefarm_project.html) in the _Terraform Provider Documentation_
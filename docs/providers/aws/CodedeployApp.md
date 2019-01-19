# Terraform::AWS::CodedeployApp

Provides a CodeDeploy application to be used as a basis for deployments

## Properties

`Name` - (Required) The name of the application.

`ComputePlatform` - (Optional) The compute platform can either be `ECS`, `Lambda`, or `Server`. Default is `Server`.


## See Also

* [aws_codedeploy_app](https://www.terraform.io/docs/providers/aws/r/codedeploy_app.html) in the _Terraform Provider Documentation_
# Terraform::AWS::ApiGatewayDeployment

Provides an API Gateway Deployment.

-> **Note:** Depends on having `Terraform::AWS::ApiGatewayIntegration` inside your rest api (which in turn depends on `awsApiGatewayMethod`). To avoid race conditions
you might need to add an explicit `depends_on = ["aws_api_gateway_integration.name"]`.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`StageName` - (Required) The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment. Use `""` to point at the default stage.

`Description` - (Optional) The description of the deployment.

`StageDescription` - (Optional) The description of the stage.

`Variables` - (Optional) A map that defines variables for the stage.


## See Also

* [aws_api_gateway_deployment](https://www.terraform.io/docs/providers/aws/r/api_gateway_deployment.html) in the _Terraform Provider Documentation_
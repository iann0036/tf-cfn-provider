# Terraform::AWS::ApiGatewayModel

Provides a Model for a API Gateway.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`Name` - (Required) The name of the model.

`Description` - (Optional) The description of the model.

`ContentType` - (Required) The content type of the model.

`Schema` - (Required) The schema of the model in a JSON form.


## Return Values

### Fn::GetAtt

`Id` - The ID of the model.

## See Also

* [aws_api_gateway_model](https://www.terraform.io/docs/providers/aws/r/api_gateway_model.html) in the _Terraform Provider Documentation_
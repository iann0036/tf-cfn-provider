# Terraform::AWS::ApiGatewayRestApi

Provides an API Gateway REST API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the REST API.

`RootResourceId` - The resource ID of the REST API's root.

`CreatedDate` - The creation date of the REST API.

`ExecutionArn` - The execution ARN part to be used in [`lambda_permission`](/docs/providers/aws/r/lambda_permission.html)'s `source_arn`.

## See Also

* [aws_api_gateway_rest_api](https://www.terraform.io/docs/providers/aws/r/api_gateway_rest_api.html) in the _Terraform Provider Documentation_
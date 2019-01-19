# Terraform::AWS::ApiGatewayDeployment

Provides an API Gateway Deployment.

-> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api (which in turn depends on `aws_api_gateway_method`). To avoid race conditions
you might need to add an explicit `depends_on = ["aws_api_gateway_integration.name"]`.

## Properties

TBC

## See Also

* [aws_api_gateway_deployment](https://www.terraform.io/docs/providers/aws/r/api_gateway_deployment.html) in the _Terraform Provider Documentation_
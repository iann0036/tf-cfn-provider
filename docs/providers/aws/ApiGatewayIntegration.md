# Terraform::AWS::ApiGatewayIntegration

Provides an HTTP Method Integration for an API Gateway Integration.

## Properties

`RestApiId` - (Required) The ID of the associated REST API.

`ResourceId` - (Required) The API resource ID.

`HttpMethod` - (Required) The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`) when calling the associated resource.

`IntegrationHttpMethod` - (Optional) The integration HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`) specifying how API Gateway will interact with the back end. **Required** if `Type` is `AWS`, `AWS_PROXY`, `HTTP` or `HTTP_PROXY`. Not all methods are compatible with all `AWS` integrations. e.g. Lambda function [can only be invoked](https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005) via `POST`.

`Type` - (Required) The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration). An `HTTP` or `HTTP_PROXY` integration with a `ConnectionType` of `VPC_LINK` is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.

`ConnectionType` - (Optional) The integration input's [connectionType](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType). Valid values are `INTERNET` (default for connections through the public routable internet), and `VPC_LINK` (for private connections between API Gateway and a network load balancer in a VPC).

`ConnectionId` - (Optional) The id of the VpcLink used for the integration. **Required** if `ConnectionType` is `VPC_LINK`.

`Uri` - (Optional) The input's URI (HTTP, AWS). **Required** if `Type` is `HTTP` or `AWS`. For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint. e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`.

`Credentials` - (Optional) The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

`RequestTemplates` - (Optional) A map of the integration's request templates.

`RequestParameters` - (Optional) A map of request query string parameters and headers that should be passed to the backend responder. For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`.

`PassthroughBehavior` - (Optional) The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `RequestTemplates` is used.

`CacheKeyParameters` - (Optional) A list of cache key parameters for the integration.

`CacheNamespace` - (Optional) The integration's cache namespace.

`RequestParametersInJson` - **Deprecated**, use `RequestParameters` instead.

`ContentHandling` - (Optional) Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

`TimeoutMilliseconds` - (Optional) Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.


## See Also

* [aws_api_gateway_integration](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html) in the _Terraform Provider Documentation_
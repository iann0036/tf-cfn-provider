# Terraform::AWS::ApiGatewayRestApi

Provides an API Gateway REST API.

## Properties

`Name` - (Required) The name of the REST API.

`Description` - (Optional) The description of the REST API.

`EndpointConfiguration` - (Optional) Nested argument defining API endpoint configuration including endpoint type. Defined below.

`BinaryMediaTypes` - (Optional) The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.

`MinimumCompressionSize` - (Optional) Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).

`Body` - (Optional) An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.

`Policy` - (Optional) JSON formatted policy document that controls access to the API Gateway. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](/docs/providers/aws/guides/iam-policy-documents.html).

`ApiKeySource` - (Optional) The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.


## Return Values

### Fn::GetAtt

`Id` - The ID of the REST API.

`RootResourceId` - The resource ID of the REST API's root.

`CreatedDate` - The creation date of the REST API.

`ExecutionArn` - The execution ARN part to be used in [`lambda_permission`](/docs/providers/aws/r/lambda_permission.html)'s `source_arn`.

## See Also

* [aws_api_gateway_rest_api](https://www.terraform.io/docs/providers/aws/r/api_gateway_rest_api.html) in the _Terraform Provider Documentation_
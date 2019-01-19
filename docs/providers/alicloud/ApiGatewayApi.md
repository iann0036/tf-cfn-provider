# Terraform::Alicloud::ApiGatewayApi

Provides an api resource.When you create an API, you must enter the basic information about the API, and define the API request information, the API backend service and response information.

For information about Api Gateway Api and how to use it, see [Create an API](https://www.alibabacloud.com/help/doc-detail/29478.htm)

~> **NOTE:** Terraform will auto build api while it uses `Terraform::Alicloud::ApiGatewayApi` to build api.

## Properties

`Name` - (Required) The name of the api gateway api. Defaults to null.

`GroupId` - (Required, ForcesNew) The api gateway that the api belongs to. Defaults to null.

`Description` - (Required) The description of the api. Defaults to null.

`AuthType` - (Required) The authorization Type including APP and ANONYMOUS. Defaults to null.

`RequestConfig` - (Required, Type: list) Request_config defines how users can send requests to your API.

`ServiceType` - (Required) The type of backend service. Type including HTTP,VPC and MOCK. Defaults to null.

`HttpServiceConfig` - (Required, Type: list) http_service_config defines the config when service_type selected 'HTTP'.

`HttpVpcServiceConfig` - (Required, Type: list) http_service_config defines the config when service_type selected 'HTTP'.

`MockServiceConfig` - (Required, Type: list) http_service_config defines the config when service_type selected 'HTTP'.

`RequestParameters` - (Required, Type: list) request_parameters defines .

`ConstantParameters` - (Required, Type: list) http_service_config defines the config when service_type selected 'HTTP'.

`SystemParameters` - (Required, Type: list) http_service_config defines the config when service_type selected 'HTTP'.

`StageNames` - (Optional, Type: list) Stages that the api need to be deployed. Valid value: RELEASE | PRE | TEST.


## Return Values

### Fn::GetAtt

`Id` - The ID of the api resource of api gateway.

`ApiId` - The ID of the api of api gateway.

## See Also

* [alicloud_api_gateway_api](https://www.terraform.io/docs/providers/alicloud/r/api_gateway_api.html) in the _Terraform Provider Documentation_
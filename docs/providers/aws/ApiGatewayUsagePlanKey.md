# Terraform::AWS::ApiGatewayUsagePlanKey

Provides an API Gateway Usage Plan Key.

## Properties

`KeyId` - (Required) The identifier of the API key resource.

`KeyType` - (Required) The type of the API key resource. Currently, the valid key type is API_KEY.

`UsagePlanId` - (Required) The Id of the usage plan resource representing to associate the key to.


## Return Values

### Fn::GetAtt

`Id` - The Id of a usage plan key.

`KeyId` - The identifier of the API gateway key resource.

`KeyType` - The type of a usage plan key. Currently, the valid key type is API_KEY.

`UsagePlanId` - The ID of the API resource.

`Name` - The name of a usage plan key.

`Value` - The value of a usage plan key.

## See Also

* [aws_api_gateway_usage_plan_key](https://www.terraform.io/docs/providers/aws/r/api_gateway_usage_plan_key.html) in the _Terraform Provider Documentation_
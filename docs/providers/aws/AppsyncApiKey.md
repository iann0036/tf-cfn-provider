# Terraform::AWS::AppsyncApiKey

Provides an AppSync API Key.

## Properties

`ApiId` - (Required) The ID of the associated AppSync API.

`Description` - (Optional) The API key description. Defaults to "Managed by Terraform".

`Expires` - (Optional) RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.


## Return Values

### Fn::GetAtt

`Id` - API Key ID (Formatted as ApiId:Key).

`Key` - The API key.

## See Also

* [aws_appsync_api_key](https://www.terraform.io/docs/providers/aws/r/appsync_api_key.html) in the _Terraform Provider Documentation_
# Terraform::AWS::DmsEndpoint

Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.

~> **Note:** All arguments including the password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`EndpointArn` - The Amazon Resource Name (ARN) for the endpoint.

## See Also

* [aws_dms_endpoint](https://www.terraform.io/docs/providers/aws/r/dms_endpoint.html) in the _Terraform Provider Documentation_
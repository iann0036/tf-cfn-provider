# Terraform::AWS::IotThing

Creates and manages an AWS IoT Thing.

## Properties

`Name` - (Required) The name of the thing.

`Attributes` - (Optional) Map of attributes of the thing.

`ThingTypeName` - (Optional) The thing type name.


## Return Values

### Fn::GetAtt

`DefaultClientId` - The default client ID.

`Version` - The current version of the thing record in the registry.

`Arn` - The ARN of the thing.

## See Also

* [aws_iot_thing](https://www.terraform.io/docs/providers/aws/r/iot_thing.html) in the _Terraform Provider Documentation_
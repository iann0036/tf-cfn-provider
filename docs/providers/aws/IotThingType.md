# Terraform::AWS::IotThingType

Creates and manages an AWS IoT Thing Type.

## Properties

`Name` - (Required, Forces New Resource) The name of the thing type.

`Description` - (Optional, Forces New Resource) The description of the thing type.

`Deprecated` - (Optional, Defaults to false) Whether the thing type is deprecated. If true, no new things could be associated with this type.

`SearchableAttributes` - (Optional, Forces New Resource) A list of searchable thing attribute names.


## Return Values

### Fn::GetAtt

`Arn` - The ARN of the created AWS IoT Thing Type.

## See Also

* [aws_iot_thing_type](https://www.terraform.io/docs/providers/aws/r/iot_thing_type.html) in the _Terraform Provider Documentation_
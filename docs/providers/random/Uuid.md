# Terraform::Random::Uuid

The resource `random_uuid` generates random uuid string that is intended to be
used as unique identifiers for other resources.

This resource uses the `hashicorp/go-uuid` to generate a UUID-formatted string
for use with services needed a unique string identifier.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Result` - The generated uuid presented in string format.

## See Also

* [random_uuid](https://www.terraform.io/docs/providers/random/r/uuid.html) in the _Terraform Provider Documentation_
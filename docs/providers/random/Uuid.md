# Terraform::Random::Uuid

The resource `Terraform::Random::Uuid` generates random uuid string that is intended to be
used as unique identifiers for other resources.

This resource uses the `hashicorp/go-uuid` to generate a UUID-formatted string
for use with services needed a unique string identifier.

## Properties

`Keepers` - (Optional) Arbitrary map of values that, when changed, will trigger a new uuid to be generated. See [the main provider documentation](../index.html) for more information.


## Return Values

### Fn::GetAtt

`Result` - The generated uuid presented in string format.

## See Also

* [random_uuid](https://www.terraform.io/docs/providers/random/r/uuid.html) in the _Terraform Provider Documentation_
# Terraform::Random::Integer

The resource `random_integer` generates random values from a given range, described by the `min` and `max` attributes of a given resource.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [random_integer](https://www.terraform.io/docs/providers/random/r/integer.html) in the _Terraform Provider Documentation_
# Terraform::Random::Id

The resource `random_id` generates random numbers that are intended to be
used as unique identifiers for other resources.

This resource *does* use a cryptographic random number generator in order
to minimize the chance of collisions, making the results of this resource
when a 16-byte identifier is requested of equivalent uniqueness to a
type-4 UUID.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`B64Url` - The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the characters `_` and `-`.

`B64Std` - The generated id presented in base64 without additional transformations.

`Hex` - The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte length.

`Dec` - The generated id presented in non-padded decimal digits.

## See Also

* [random_id](https://www.terraform.io/docs/providers/random/r/id.html) in the _Terraform Provider Documentation_
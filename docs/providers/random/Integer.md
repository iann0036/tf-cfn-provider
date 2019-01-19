# Terraform::Random::Integer

The resource `Terraform::Random::Integer` generates random values from a given range, described by the `Min` and `Max` attributes of a given resource.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Properties

`Min` - (int) The minimum inclusive value of the range.

`Max` - (int) The maximum inclusive value of the range.

`Keepers` - (Optional) Arbitrary map of values that, when changed, will trigger a new id to be generated. See [the main provider documentation](../index.html) for more information.

`Seed` - (Optional) A custom seed to always produce the same value.


## See Also

* [random_integer](https://www.terraform.io/docs/providers/random/r/integer.html) in the _Terraform Provider Documentation_
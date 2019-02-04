# Terraform::Random::Pet

The resource `Terraform::Random::Pet` generates random pet names that are intended to be
used as unique identifiers for other resources.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Properties

`Keepers` - (Optional) Arbitrary map of values that, when changed, will
trigger a new id to be generated. See
[the main provider documentation](../index.html) for more information.

`Length` - (Optional) The length (in words) of the pet name.

`Prefix` - (Optional) A string to prefix the name with.

`Separator` - (Optional) The character to separate words in the pet name.


## See Also

* [random_pet](https://www.terraform.io/docs/providers/random/r/pet.html) in the _Terraform Provider Documentation_
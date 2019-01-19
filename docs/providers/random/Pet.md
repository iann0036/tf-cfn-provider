# Terraform::Random::Pet

The resource `random_pet` generates random pet names that are intended to be
used as unique identifiers for other resources.

This resource can be used in conjunction with resources that have
the `create_before_destroy` lifecycle flag set, to avoid conflicts with
unique names during the brief period where both the old and new resources
exist concurrently.

## Properties

TBC

## See Also

* [random_pet](https://www.terraform.io/docs/providers/random/r/pet.html) in the _Terraform Provider Documentation_
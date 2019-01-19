# Terraform::Random::String

The resource `Terraform::Random::String` generates a random permutation of alphanumeric
characters and optionally special characters.

This resource *does* use a cryptographic random number generator.

## Properties

`Length` - (Required) The length of the string desired.

`Upper` - (Optional) (default true) Include uppercase alphabet characters in random string.

`MinUpper` - (Optional) (default 0) Minimum number of uppercase alphabet characters in random string.

`Lower` - (Optional) (default true) Include lowercase alphabet characters in random string.

`MinLower` - (Optional) (default 0) Minimum number of lowercase alphabet characters in random string.

`Number` - (Optional) (default true) Include numeric characters in random string.

`MinNumeric` - (Optional) (default 0) Minimum number of numeric characters in random string.

`Special` - (Optional) (default true) Include special characters in random string. These are '!@#$%&*()-_=+[]{}<>:?'.

`MinSpecial` - (Optional) (default 0) Minimum number of special characters in random string.

`OverrideSpecial` - (Optional) Supply your own list of special characters to use for string generation.  This overrides characters list in the special argument.  The special argument must still be set to true for any overwritten characters to be used in generation.

`Keepers` - (Optional) Arbitrary map of values that, when changed, will trigger a new id to be generated. See [the main provider documentation](../index.html) for more information.


## Return Values

### Fn::GetAtt

`Result` - Random string generated.

## See Also

* [random_string](https://www.terraform.io/docs/providers/random/r/string.html) in the _Terraform Provider Documentation_
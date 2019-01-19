# Terraform::Random::Shuffle

The resource `Terraform::Random::Shuffle` generates a random permutation of a list
of strings given as an argument.

## Properties

`Input` - (Required) The list of strings to shuffle.

`ResultCount` - (Optional) The number of results to return. Defaults to the number of items in the `Input` list. If fewer items are requested, some elements will be excluded from the result. If more items are requested, items will be repeated in the result but not more frequently than the number of items in the input list.

`Keepers` - (Optional) Arbitrary map of values that, when changed, will trigger a new id to be generated. See [the main provider documentation](../index.html) for more information.

`Seed` - (Optional) Arbitrary string with which to seed the random number generator, in order to produce less-volatile permutations of the list. **Important:** Even with an identical seed, it is not guaranteed that the same permutation will be produced across different versions of Terraform. This argument causes the result to be *less volatile*, but not fixed for all time.


## Return Values

### Fn::GetAtt

`Result` - Random permutation of the list of strings given in `Input`.

## See Also

* [random_shuffle](https://www.terraform.io/docs/providers/random/r/shuffle.html) in the _Terraform Provider Documentation_
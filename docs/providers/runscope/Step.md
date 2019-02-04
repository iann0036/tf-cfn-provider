# Terraform::RunScope::Step

A [step](https://www.runscope.com/docs/api/steps) resource.
API tests are comprised of a series of steps, most often HTTP requests.
In addition to requests, you can also add additional types of steps to
your tests like pauses and conditions.

## Properties

`BucketId` - (Required) The id of the bucket to associate this step with.

`TestId` - (Required) The id of the test to associate this step with.

`Note` - (Optional) A comment attached to the test step.

`StepType` - (Required) The type of step.


## Return Values

### Fn::GetAtt

`Id` - The ID of the step.

## See Also

* [runscope_step](https://www.terraform.io/docs/providers/runscope/r/step.html) in the _Terraform Provider Documentation_
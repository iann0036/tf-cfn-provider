# Terraform::RunScope::Environment

An [environment](https://www.runscope.com/docs/api/environments) resource.
An [environment](https://www.runscope.com/docs/api-testing/environments)
is is a group of configuration settings (initial variables, locations,
notifications, integrations, etc.) used when running a test.
Every test has at least one environment, but you can create additional
environments as needed. For common settings (base URLs, API keys)
that you'd like to use across all tests within a bucket,
use a [Shared Environment](https://www.runscope.com/docs/api-testing/environments#shared).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the environment.

## See Also

* [runscope_environment](https://www.terraform.io/docs/providers/runscope/r/environment.html) in the _Terraform Provider Documentation_
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

`BucketId` - (Required) The id of the bucket to associate this environment with.

`TestId` - (Optional) The id of the test to associate this environment with. If given, creates a test specific environment, otherwise creates a shared environment.

`Name` - (Required) The name of environment.

`Script` - (Optional) The [script](https://www.runscope.com/docs/api-testing/scripts#initial-script) to to run to setup the environment.

`PreserveCookies` - (Optional) If this is set to true, tests using this enviornment will manage cookies between steps.

`InitialVariables` - (Optional) Map of keys and values being used for variables when the test begins.

`Integrations` - (Optional) A list of integration ids to enable for test runs using this environment.

`Regions` - (Optional) A list of [Runscope regions](https://www.runscope.com/docs/regions) to execute test runs in when using this environment.

`RemoteAgents` - (Optional) A list of [Remote Agents](https://www.runscope.com/docs/api/agents) to execute test runs in when using this environment. Remote Agents documented below.

### RemoteAgents Properties

`Name` - (Required) The name of the remote agent.

`Uuid` - (Required) The uuid of the remote agent.

### Emails Properties

`NotifyAll` - (Required) Send an email to all team members according to the `NotifyOn` rules.

`NotifyOn` - (Required) Upon completion of a test run Runscope will send email notifications, allowed values: `all`, `failures`, `threshold` or `switch`.

### Recipients Properties

`Name` - (Optional) The name of the person.

`Id` - (Optional) The unique identifier for this person's account.

`Email` - (Optional) The email address for this account.


## Return Values

### Fn::GetAtt

`Id` - The ID of the environment.

## See Also

* [runscope_environment](https://www.terraform.io/docs/providers/runscope/r/environment.html) in the _Terraform Provider Documentation_
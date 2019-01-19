# Terraform::Rundeck::Project

The project resource allows Rundeck projects to be managed by Terraform. In Rundeck a project
is the container object for a set of jobs and the configuration for which servers those jobs
can be run on.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Name` - The unique name that identifies the project, as set in the arguments.

`UiUrl` - The URL of the index page for this project in the Rundeck UI.

## See Also

* [rundeck_project](https://www.terraform.io/docs/providers/rundeck/r/project.html) in the _Terraform Provider Documentation_
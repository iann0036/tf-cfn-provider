# Terraform::Rundeck::Project

The project resource allows Rundeck projects to be managed by Terraform. In Rundeck a project
is the container object for a set of jobs and the configuration for which servers those jobs
can be run on.

## Properties

`Name` - (Required) The name of the project, used both in the UI and to uniquely identify the project. Must therefore be unique across a single Rundeck installation.

`ResourceModelSource` - (Required) Nested block instructing Rundeck on how to determine the set of resources (nodes) for this project. The nested block structure is described below.

`Description` - (Optional) A description of the project, to be displayed in the Rundeck UI. Defaults to "Managed by Terraform".

`DefaultNodeFileCopierPlugin` - (Optional) The name of a plugin to use to copy files onto nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol to send files over SSH.

`DefaultNodeExecutorPlugin` - (Optional) The name of a plugin to use to run commands on nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the nodes.

`SshAuthenticationType` - (Optional) When the SSH-based file copier and executor plugins are used, the type of SSH authentication to use. Defaults to `privateKey`.

`SshKeyStoragePath` - (Optional) When the SSH-based file copier and executor plugins are used, the location within Rundeck's key store where the SSH private key can be found. Private keys can be uploaded to rundeck using the `Terraform::Rundeck::PrivateKey` resource.

`SshKeyFilePath` - (Optional) Like `SshKeyStoragePath` except that the key is read from the Rundeck server's local filesystem, rather than from the key store.

`ExtraConfig` - (Optional) Behind the scenes a Rundeck project is really an arbitrary set of key/value pairs. This map argument allows setting any configuration properties that aren't explicitly supported by the other arguments described above, but due to limitations of Terraform the key names must be written with slashes in place of dots. Do not use this argument to set properties that the above arguments set, or undefined behavior will result.

### ResourceModelSource Properties

`Type` - (Required) The name of the resource model plugin to use.

`Config` - (Required) Map of arbitrary configuration properties for the selected resource model plugin.


## Return Values

### Fn::GetAtt

`Name` - The unique name that identifies the project, as set in the arguments.

`UiUrl` - The URL of the index page for this project in the Rundeck UI.

## See Also

* [rundeck_project](https://www.terraform.io/docs/providers/rundeck/r/project.html) in the _Terraform Provider Documentation_
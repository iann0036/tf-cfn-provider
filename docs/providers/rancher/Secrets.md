# Terraform::Rancher::Secrets

Provides a Rancher Secret resource. This can be used to create secrets for rancher environments and retrieve their information.

## Properties

`Name` - (Required) The name of the secret.

`Description` - (Optional) A description of the secret.

`EnvironmentId` - (Required) The ID of the environment to create the secret for.

`Value` - (Required) The secret value.


## See Also

* [rancher_secrets](https://www.terraform.io/docs/providers/rancher/r/secrets.html) in the _Terraform Provider Documentation_
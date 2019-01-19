# Terraform::Rancher::RegistrationToken

Provides a Rancher Registration Token resource. This can be used to create registration tokens for rancher environments and retrieve their information.

## Properties

`Name` - (Required) The name of the registration token.

`Description` - (Optional) A registration token description.

`EnvironmentId` - (Required) The ID of the environment to create the token for.

`HostLabels` - (Optional) A map of host labels to add to the registration command.

`AgentIp` - (Optional) A string containing the CATTLE_AGENT_IP to add to the registration command.


## Return Values

### Fn::GetAtt

`Id` - (Computed) The ID of the resource.

`Image` - (Computed).

`Command` - The command used to start a rancher agent for this environment.

`RegistrationUrl` - The URL to use to register new nodes to the environment.

`Token` - The token to use to register new nodes to the environment.

## See Also

* [rancher_registration_token](https://www.terraform.io/docs/providers/rancher/r/registration_token.html) in the _Terraform Provider Documentation_
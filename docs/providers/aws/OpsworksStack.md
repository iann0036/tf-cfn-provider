# Terraform::AWS::OpsworksStack

Provides an OpsWorks stack resource.

## Properties

`Name` - (Required) The name of the stack.

`Region` - (Required) The name of the region where the stack will exist.

`ServiceRoleArn` - (Required) The ARN of an IAM role that the OpsWorks service will act as.

`DefaultInstanceProfileArn` - (Required) The ARN of an IAM Instance Profile that created instances will have by default.

`AgentVersion` - (Optional) If set to `"LATEST"`, OpsWorks will automatically install the latest version.

`BerkshelfVersion` - (Optional) If `ManageBerkshelf` is enabled, the version of Berkshelf to use.

`Color` - (Optional) Color to paint next to the stack's resources in the OpsWorks console.

`DefaultAvailabilityZone` - (Optional) Name of the availability zone where instances will be created by default. This is required unless you set `VpcId`.

`ConfigurationManagerName` - (Optional) Name of the configuration manager to use. Defaults to "Chef".

`ConfigurationManagerVersion` - (Optional) Version of the configuration manager to use. Defaults to "11.4".

`CustomCookbooksSource` - (Optional) When `UseCustomCookbooks` is set, provide this sub-object as described below.

`CustomJson` - (Optional) User defined JSON passed to "Chef". Use a "here doc" for multiline JSON.

`DefaultOs` - (Optional) Name of OS that will be installed on instances by default.

`DefaultRootDeviceType` - (Optional) Name of the type of root device instances will have by default.

`DefaultSshKeyName` - (Optional) Name of the SSH keypair that instances will have by default.

`DefaultSubnetId` - (Optional) Id of the subnet in which instances will be created by default. Mandatory if `VpcId` is set, and forbidden if it isn't.

`HostnameTheme` - (Optional) Keyword representing the naming scheme that will be used for instance hostnames within this stack.

`ManageBerkshelf` - (Optional) Boolean value controlling whether Opsworks will run Berkshelf for this stack.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`UseCustomCookbooks` - (Optional) Boolean value controlling whether the custom cookbook settings are enabled.

`UseOpsworksSecurityGroups` - (Optional) Boolean value controlling whether the standard OpsWorks security groups apply to created instances.

`VpcId` - (Optional) The id of the VPC that this stack belongs to.

`CustomJson` - (Optional) Custom JSON attributes to apply to the entire stack.

### CustomCookbooksSource Properties

`Type` - (Required) The type of source to use. For example, "archive".

`Url` - (Required) The URL where the cookbooks resource can be found.

`Username` - (Optional) Username to use when authenticating to the source.

`Password` - (Optional) Password to use when authenticating to the source.

`SshKey` - (Optional) SSH key to use when authenticating to the source.

`Revision` - (Optional) For sources that are version-aware, the revision to use.


## Return Values

### Fn::GetAtt

`Id` - The id of the stack.

## See Also

* [aws_opsworks_stack](https://www.terraform.io/docs/providers/aws/r/opsworks_stack.html) in the _Terraform Provider Documentation_
# Terraform::AWS::DirectoryServiceDirectory

Provides a Simple or Managed Microsoft directory in AWS Directory Service.

~> **Note:** All arguments including the password and customer username will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) The fully qualified name for the directory, such as `corp.example.com`.

`Password` - (Required) The password for the directory administrator or connector user.

`Size` - (Required for `SimpleAD` and `ADConnector`) The size of the directory (`Small` or `Large` are accepted values).

`VpcSettings` - (Required for `SimpleAD` and `MicrosoftAD`) VPC related information about the directory. Fields documented below.

`ConnectSettings` - (Required for `ADConnector`) Connector related information about the directory. Fields documented below.

`Alias` - (Optional) The alias for the directory (must be unique amongst all aliases in AWS). Required for `EnableSso`.

`Description` - (Optional) A textual description for the directory.

`ShortName` - (Optional) The short name of the directory, such as `CORP`.

`EnableSso` - (Optional) Whether to enable single-sign on for the directory. Requires `Alias`. Defaults to `false`.

`Edition` - (Optional) The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

`Tags` - (Optional) A mapping of tags to assign to the resource.

`SubnetIds` - (Required) The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).

`VpcId` - (Required) The identifier of the VPC that the directory is in.

`CustomerUsername` - (Required) The username corresponding to the password provided.

`CustomerDnsIps` - (Required) The DNS IP addresses of the domain to connect to.

`SubnetIds` - (Required) The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).

`VpcId` - (Required) The identifier of the VPC that the directory is in.


## Return Values

### Fn::GetAtt

`Id` - The directory identifier.

`AccessUrl` - The access URL for the directory, such as `http://alias.awsapps.com`.

`DnsIpAddresses` - A list of IP addresses of the DNS servers for the directory or connector.

`SecurityGroupId` - The ID of the security group created by the directory (`SimpleAD` or `MicrosoftAD` only).

## See Also

* [aws_directory_service_directory](https://www.terraform.io/docs/providers/aws/r/directory_service_directory.html) in the _Terraform Provider Documentation_
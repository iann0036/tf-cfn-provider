# Terraform::AWS::DirectoryServiceDirectory

Provides a Simple or Managed Microsoft directory in AWS Directory Service.

~> **Note:** All arguments including the password and customer username will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The directory identifier.

`AccessUrl` - The access URL for the directory, such as `http://alias.awsapps.com`.

`DnsIpAddresses` - A list of IP addresses of the DNS servers for the directory or connector.

`SecurityGroupId` - The ID of the security group created by the directory (`SimpleAD` or `MicrosoftAD` only).

## See Also

* [aws_directory_service_directory](https://www.terraform.io/docs/providers/aws/r/directory_service_directory.html) in the _Terraform Provider Documentation_
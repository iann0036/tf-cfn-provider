# Terraform::AWS::DirectoryServiceConditionalForwarder

Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.

## Properties

`DirectoryId` - (Required) The id of directory.

`DnsIps` - (Required) A list of forwarder IP addresses.

`RemoteDomainName` - (Required) The fully qualified domain name of the remote domain for which forwarders will be used.


## See Also

* [aws_directory_service_conditional_forwarder](https://www.terraform.io/docs/providers/aws/r/directory_service_conditional_forwarder.html) in the _Terraform Provider Documentation_
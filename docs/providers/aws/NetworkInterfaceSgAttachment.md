# Terraform::AWS::NetworkInterfaceSgAttachment

This resource attaches a security group to an Elastic Network Interface (ENI).
It can be used to attach a security group to any existing ENI, be it a
secondary ENI or one attached as the primary interface on an instance.

~> **NOTE on instances, interfaces, and security groups:** Terraform currently
provides the capability to assign security groups via the [`Terraform::AWS::Instance`][1]
and the [`Terraform::AWS::NetworkInterface`][2] resources. Using this resource in
conjunction with security groups provided in-line in those resources will cause
conflicts, and will lead to spurious diffs and undefined behavior - please use
one or the other.

[1]: /docs/providers/aws/d/instance.html
[2]: /docs/providers/aws/r/network_interface.html

## Properties

`SecurityGroupId` - (Required) The ID of the security group.

`NetworkInterfaceId` - (Required) The ID of the network interface to attach to.


## See Also

* [aws_network_interface_sg_attachment](https://www.terraform.io/docs/providers/aws/r/network_interface_sg_attachment.html) in the _Terraform Provider Documentation_
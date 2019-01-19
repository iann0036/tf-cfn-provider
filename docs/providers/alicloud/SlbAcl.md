# Terraform::Alicloud::SlbAcl

An access control list contains multiple IP addresses or CIDR blocks.
The access control list can help you to define multiple instance listening dimension,
and to meet the multiple usage for single access control list.

Server Load Balancer allows you to configure access control for listeners.
You can configure different whitelists or blacklists for different listeners.

You can configure access control
when you create a listener or change access control configuration after a listener is created.

~> **NOTE:** One access control list can be attached to many Listeners in different load balancer as whitelists or blacklists.

~> **NOTE:** The maximum number of access control lists per region  is 50.

~> **NOTE:** The maximum number of IP addresses added each time is 50.

~> **NOTE:** The maximum number of entries per access control list is 300.

~> **NOTE:** The maximum number of listeners that an access control list can be added to is 50.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about acl and how to use it, see [Configure an access control list](https://www.alibabacloud.com/help/doc-detail/85978.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Id of the access control list.

## See Also

* [alicloud_slb_acl](https://www.terraform.io/docs/providers/alicloud/r/slb_acl.html) in the _Terraform Provider Documentation_
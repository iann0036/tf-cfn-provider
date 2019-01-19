# Terraform::Alicloud::CenInstance

Provides a CEN instance resource. Cloud Enterprise Network (CEN) is a service that allows you to create a global network for rapidly building a distributed business system with a hybrid cloud computing solution. CEN enables you to build a secure, private, and enterprise-class interconnected network between VPCs in different regions and your local data centers. CEN provides enterprise-class scalability that automatically responds to your dynamic computing requirements.

For information about CEN and how to use it, see [What is Cloud Enterprise Network](https://www.alibabacloud.com/help/doc-detail/59870.htm).

## Properties

`Name` - (Optional) The name of the CEN instance. Defaults to null.

`Description` - (Optional) The description of the CEN instance. Defaults to null.


## Return Values

### Fn::GetAtt

`Id` - The ID of the CEN instance.

`Name` - The name of the CEN instance.

`Description` - The description of the CEN instance.

## See Also

* [alicloud_cen_instance](https://www.terraform.io/docs/providers/alicloud/r/cen_instance.html) in the _Terraform Provider Documentation_
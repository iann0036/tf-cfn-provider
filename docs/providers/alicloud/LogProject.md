# Terraform::Alicloud::LogProject

The project is the resource management unit in Log Service and is used to isolate and control resources.
You can manage all the logs and the related log sources of an application by using projects. [Refer to details](https://www.alibabacloud.com/help/doc-detail/48873.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the log project. It sames as its name.

`Name` - Log project name.

`Description` - Log project description.

## See Also

* [alicloud_log_project](https://www.terraform.io/docs/providers/alicloud/r/log_project.html) in the _Terraform Provider Documentation_
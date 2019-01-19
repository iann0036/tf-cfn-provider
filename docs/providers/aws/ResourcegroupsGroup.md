# Terraform::AWS::ResourcegroupsGroup

Provides a Resource Group.

## Properties

`Name` - (Required) The resource group's name. A resource group name can have a maximum of 127 characters, including letters, numbers, hyphens, dots, and underscores. The name cannot start with `AWS` or `aws`.

`Description` - (Optional) A description of the resource group.

`ResourceQuery` - (Required) A `ResourceQuery` block. Resource queries are documented below.

### ResourceQuery Properties

`Query` - (Required) The resource query as a JSON string.

`Type` - (Required) The type of the resource query. Defaults to `TAG_FILTERS_1_0`.


## Return Values

### Fn::GetAtt

`Arn` - The ARN assigned by AWS for this resource group.

## See Also

* [aws_resourcegroups_group](https://www.terraform.io/docs/providers/aws/r/resourcegroups_group.html) in the _Terraform Provider Documentation_
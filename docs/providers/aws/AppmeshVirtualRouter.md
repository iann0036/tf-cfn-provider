# Terraform::AWS::AppmeshVirtualRouter

Provides an AWS App Mesh virtual router resource.

## Properties

`Name` - (Required) The name to use for the virtual router.

`MeshName` - (Required) The name of the service mesh in which to create the virtual router.

`Spec` - (Required) The virtual router specification to apply.

### Spec Properties

`ServiceNames` - (Required) The service mesh service names to associate with the virtual router.


## Return Values

### Fn::GetAtt

`Id` - The ID of the virtual router.

`Arn` - The ARN of the virtual router.

`CreatedDate` - The creation date of the virtual router.

`LastUpdatedDate` - The last update date of the virtual router.

## See Also

* [aws_appmesh_virtual_router](https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_router.html) in the _Terraform Provider Documentation_
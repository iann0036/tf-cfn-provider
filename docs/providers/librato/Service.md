# Terraform::Librato::Service

Provides a Librato Service resource. This can be used to
create and manage notification services on Librato.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the alert.

`Type` - The type of notificaion.

`Title` - The alert title.

`Settings` - a JSON hash of settings specific to the alert type.

## See Also

* [librato_service](https://www.terraform.io/docs/providers/librato/r/service.html) in the _Terraform Provider Documentation_
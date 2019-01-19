# Terraform::Librato::Service

Provides a Librato Service resource. This can be used to
create and manage notification services on Librato.

## Properties

`Type` - (Required) The type of notificaion.

`Title` - (Required) The alert title.

`Settings` - (Required) a JSON hash of settings specific to the alert type.


## Return Values

### Fn::GetAtt

`Id` - The ID of the alert.

`Type` - The type of notificaion.

`Title` - The alert title.

`Settings` - a JSON hash of settings specific to the alert type.

## See Also

* [librato_service](https://www.terraform.io/docs/providers/librato/r/service.html) in the _Terraform Provider Documentation_
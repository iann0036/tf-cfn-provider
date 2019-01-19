# Terraform::AWS::GameliftAlias

Provides a Gamelift Alias resource.

## Properties

`Name` - (Required) Name of the alias.

`Description` - (Optional) Description of the alias.

`RoutingStrategy` - (Required) Specifies the fleet and/or routing type to use for the alias.


## Return Values

### Fn::GetAtt

`Id` - Alias ID.

`Arn` - Alias ARN.

## See Also

* [aws_gamelift_alias](https://www.terraform.io/docs/providers/aws/r/gamelift_alias.html) in the _Terraform Provider Documentation_
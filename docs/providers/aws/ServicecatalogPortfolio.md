# Terraform::AWS::ServicecatalogPortfolio

Provides a resource to create a Service Catalog Portfolio.

## Properties

`Name` - (Required) The name of the portfolio.

`Description` - (Required) Description of the portfolio.

`ProviderName` - (Required) Name of the person or organization who owns the portfolio.

`Tags` - (Optional) Tags to apply to the connection.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Service Catalog Portfolio.

## See Also

* [aws_servicecatalog_portfolio](https://www.terraform.io/docs/providers/aws/r/servicecatalog_portfolio.html) in the _Terraform Provider Documentation_
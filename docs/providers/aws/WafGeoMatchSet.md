# Terraform::AWS::WafGeoMatchSet

Provides a WAF Geo Match Set Resource

## Properties

`Name` - (Required) The name or description of the GeoMatchSet.

`GeoMatchConstraint` - (Optional) The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.


## Return Values

### Fn::GetAtt

`Id` - The ID of the WAF GeoMatchSet.

## See Also

* [aws_waf_geo_match_set](https://www.terraform.io/docs/providers/aws/r/waf_geo_match_set.html) in the _Terraform Provider Documentation_
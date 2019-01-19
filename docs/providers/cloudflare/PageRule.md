# Terraform::Cloudflare::PageRule

Provides a Cloudflare page rule resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The page rule ID.

`ZoneId` - The ID of the zone in which the page rule will be applied.

`Target` - The URL pattern targeted by the page rule.

`Actions` - The actions applied by the page rule.

`Priority` - The priority of the page rule.

`Status` - Whether the page rule is active or disabled.

## See Also

* [cloudflare_page_rule](https://www.terraform.io/docs/providers/cloudflare/r/page_rule.html) in the _Terraform Provider Documentation_
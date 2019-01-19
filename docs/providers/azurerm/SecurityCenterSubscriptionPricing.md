# Terraform::AzureRM::SecurityCenterSubscriptionPricing

Manages the Pricing Tier for Azure Security Center in the current subscription.

~> **NOTE:** This resource requires the `Owner` permission on the Subscription.

~> **NOTE:** Deletion of this resource does not change or reset the pricing tier to `Free`

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The subscription pricing ID.

## See Also

* [azurerm_security_center_subscription_pricing](https://www.terraform.io/docs/providers/azurerm/r/security_center_subscription_pricing.html) in the _Terraform Provider Documentation_
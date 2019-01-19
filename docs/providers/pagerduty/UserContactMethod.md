# Terraform::PagerDuty::UserContactMethod

A [contact method](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users_id_contact_methods) is a contact method for a PagerDuty user (email, phone or SMS).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the contact method.

`Blacklisted` - If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it.

`Enabled` - If true, this phone is capable of receiving SMS messages.

## See Also

* [pagerduty_user_contact_method](https://www.terraform.io/docs/providers/pagerduty/r/user_contact_method.html) in the _Terraform Provider Documentation_
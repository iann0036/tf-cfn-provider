# Terraform::PagerDuty::UserContactMethod

A [contact method](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users_id_contact_methods) is a contact method for a PagerDuty user (email, phone or SMS).

## Properties

`UserId` - (Required) The ID of the user.
* `Type` - (Required) The contact method type. May be (`email_contact_method`, `phone_contact_method`, `sms_contact_method`, `push_notification_contact_method`).
* `SendShortEmail` - (Optional) Send an abbreviated email message instead of the standard email output.
* `CountryCode` - (Optional) The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `Label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `Address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

`Type` - (Required) The contact method type. May be (`email_contact_method`, `phone_contact_method`, `sms_contact_method`, `push_notification_contact_method`).
* `SendShortEmail` - (Optional) Send an abbreviated email message instead of the standard email output.
* `CountryCode` - (Optional) The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `Label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `Address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

`SendShortEmail` - (Optional) Send an abbreviated email message instead of the standard email output.
* `CountryCode` - (Optional) The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `Label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `Address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

`CountryCode` - (Optional) The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `Label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `Address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

`Label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `Address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

`Address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.


## Return Values

### Fn::GetAtt

`Id` - The ID of the contact method.

`Blacklisted` - If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it.

`Enabled` - If true, this phone is capable of receiving SMS messages.

## See Also

* [pagerduty_user_contact_method](https://www.terraform.io/docs/providers/pagerduty/r/user_contact_method.html) in the _Terraform Provider Documentation_
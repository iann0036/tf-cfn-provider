# Terraform::AWS::CognitoUserPool

Provides a Cognito User Pool resource.

## Properties

`AliasAttributes` - (Optional) Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `UsernameAttributes`.

`AutoVerifiedAttributes` - (Optional) The attributes to be auto-verified. Possible values: email, phone_number.

`Name` - (Required) The name of the user pool.

`EmailVerificationSubject` - (Optional) A string representing the email verification subject. **NOTE:** - If `EmailVerificationSubject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

`EmailVerificationMessage` - (Optional) A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `EmailVerificationMessage` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

`MfaConfiguration` - (Optional, Default: OFF) Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL).

`SmsAuthenticationMessage` - (Optional) A string representing the SMS authentication message.

`SmsVerificationMessage` - (Optional) A string representing the SMS verification message.

`Tags` - (Optional) A mapping of tags to assign to the User Pool.

`UsernameAttributes` - (Optional) Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `AliasAttributes`.


## See Also

* [aws_cognito_user_pool](https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html) in the _Terraform Provider Documentation_
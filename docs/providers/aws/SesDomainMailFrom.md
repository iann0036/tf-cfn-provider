# Terraform::AWS::SesDomainMailFrom

Provides an SES domain MAIL FROM resource.

~> **NOTE:** For the MAIL FROM domain to be fully usable, this resource should be paired with the [aws_ses_domain_identity resource](/docs/providers/aws/r/ses_domain_identity.html). To validate the MAIL FROM domain, a DNS MX record is required. To pass SPF checks, a DNS TXT record may also be required. See the [Amazon SES MAIL FROM documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html) for more information.

## Properties

`Domain` - (Required) Verified domain name to generate DKIM tokens for.

`MailFromDomain` - (Required) Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation).

`BehaviorOnMxFailure` - (Optional) The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.


## Return Values

### Fn::GetAtt

`Id` - The domain name.

## See Also

* [aws_ses_domain_mail_from](https://www.terraform.io/docs/providers/aws/r/ses_domain_mail_from.html) in the _Terraform Provider Documentation_
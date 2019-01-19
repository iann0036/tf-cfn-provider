# Terraform::AWS::SesDomainMailFrom

Provides an SES domain MAIL FROM resource.

~> **NOTE:** For the MAIL FROM domain to be fully usable, this resource should be paired with the [aws_ses_domain_identity resource](/docs/providers/aws/r/ses_domain_identity.html). To validate the MAIL FROM domain, a DNS MX record is required. To pass SPF checks, a DNS TXT record may also be required. See the [Amazon SES MAIL FROM documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html) for more information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The domain name.

## See Also

* [aws_ses_domain_mail_from](https://www.terraform.io/docs/providers/aws/r/ses_domain_mail_from.html) in the _Terraform Provider Documentation_
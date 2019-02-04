# Terraform::Mailgun::Domain

Provides a Mailgun App resource. This can be used to
create and manage applications on Mailgun.

## Properties

`Name` - (Required) The domain to add to Mailgun.

`SmtpPassword` - (Required) Password for SMTP authentication.

`SpamAction` - (Optional) `disabled` or `tag` Disable, no spam
filtering will occur for inbound messages. Tag, messages
will be tagged with a spam header.

`Wildcard` - (Optional) Boolean that determines whether
the domain will accept email for sub-domains.


## Return Values

### Fn::GetAtt

`Name` - The name of the record.

`SmtpLogin` - The login email for the SMTP server.

`SmtpPassword` - The password to the SMTP server.

`Wildcard` - Whether or not the domain will accept email for sub-domains.

`SpamAction` - The spam filtering setting.

`ReceivingRecords` - A list of DNS records for receiving validation.

`Priority` - The priority of the record.

`RecordType` - The record type.

`Valid` - `"valid"` if the record is valid.

`Value` - The value of the record.

`SendingRecords` - A list of DNS records for sending validation.

## See Also

* [mailgun_domain](https://www.terraform.io/docs/providers/mailgun/r/domain.html) in the _Terraform Provider Documentation_
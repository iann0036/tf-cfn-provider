# Terraform::AWS::LightsailDomain

Creates a domain resource for the specified domain (e.g., example.com).
You cannot register a new domain name using Lightsail. You must register
a domain name using Amazon Route 53 or another domain name registrar.
If you have already registered your domain, you can enter its name in
this parameter to manage the DNS records for that domain.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The name used for this domain.

`Arn` - The ARN of the Lightsail domain.

## See Also

* [aws_lightsail_domain](https://www.terraform.io/docs/providers/aws/r/lightsail_domain.html) in the _Terraform Provider Documentation_
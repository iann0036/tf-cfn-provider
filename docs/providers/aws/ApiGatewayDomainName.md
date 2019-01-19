# Terraform::AWS::ApiGatewayDomainName

Registers a custom domain name for use with AWS API Gateway.

This resource just establishes ownership of and the TLS settings for
a particular domain name. An API can be attached to a particular path
under the registered domain name using
[the `Terraform::AWS::ApiGatewayBasePathMapping` resource](api_gateway_base_path_mapping.html).

API Gateway domains can be defined as either 'edge-optimized' or 'regional'.  In an edge-optimized configuration,
API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
addition to this resource it's necessary to create a DNS record corresponding to the given domain name which is an alias
(either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the `cloudfront_domain_name`
attribute.

In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
the `regional_domain_name` attribute.

~> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`DomainName` - (Required) The fully-qualified domain name to register.

`EndpointConfiguration` - (Optional) Configuration block defining API endpoint information including type. Defined below.

`CertificateArn` - (Optional) The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `CertificateName`, `CertificateBody`, `CertificateChain`, `CertificatePrivateKey`, `RegionalCertificateArn`, and `RegionalCertificateName`.

`RegionalCertificateArn` - (Optional) The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `CertificateArn`, `CertificateName`, `CertificateBody`, `CertificateChain`, and `CertificatePrivateKey`.

`CertificateName` - (Optional) The unique name to use when registering this certificate as an IAM server certificate. Conflicts with `CertificateArn`, `RegionalCertificateArn`, and `RegionalCertificateName`. Required if `CertificateArn` is not set.

`CertificateBody` - (Optional) The certificate issued for the domain name being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `CertificateArn`, `RegionalCertificateArn`, and `RegionalCertificateName`.

`CertificateChain` - (Optional) The certificate for the CA that issued the certificate, along with any intermediate CA certificates required to create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `CertificateArn`, `RegionalCertificateArn`, and `RegionalCertificateName`.

`CertificatePrivateKey` - (Optional) The private key associated with the domain certificate given in `CertificateBody`. Only valid for `EDGE` endpoint configuration type. Conflicts with `CertificateArn`, `RegionalCertificateArn`, and `RegionalCertificateName`.

`RegionalCertificateName` - (Optional) The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `CertificateArn`, `CertificateName`, `CertificateBody`, `CertificateChain`, and `CertificatePrivateKey`.


## Return Values

### Fn::GetAtt

`Id` - The internal id assigned to this domain name by API Gateway.

`CertificateUploadDate` - The upload date associated with the domain certificate.

`CloudfrontDomainName` - The hostname created by Cloudfront to represent.

`CloudfrontZoneId` - For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`).

`RegionalDomainName` - The hostname for the custom domain's regional endpoint.

`RegionalZoneId` - The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.

## See Also

* [aws_api_gateway_domain_name](https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name.html) in the _Terraform Provider Documentation_
# Terraform::OCI::LoadBalancerCertificate

This resource provides the Certificate resource in Oracle Cloud Infrastructure Load Balancer service.

Creates an asynchronous request to add an SSL certificate bundle.

Set the terraform flag `lifecycle { create_before_destroy = true }` in your certificate to facilitate rotating certificates. 
A certificate cannot be deleted if it is attached to another resource (a listener or a backend set for example).
Because certificate_name in the listener is an updatable parameter, terraform will attempt to recreate the certificate first and then update the listener but the certificate cannot be deleted while it is attached to a listener so it will fail.
Setting the flag makes it so that when a certificate is recreated, the new certificate will be created first before the old one gets deleted.
Whenever you change any values on a certificate that causes it to be recreated the certificate_name MUST also change. Otherwise you will get an error saying that a certificate with that name already exists.

## Properties

`CaCertificate` - (Optional) The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

`CertificateName` - (Required) A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.  Example: `example_certificate_bundle`.

`LoadBalancerId` - (Required) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the load balancer on which to add the certificate bundle.

`Passphrase` - (Optional) A passphrase for encrypted private keys. This is needed only if you created your certificate with a passphrase.

`PrivateKey` - (Optional) The SSL private key for your certificate, in PEM format.

`PublicCertificate` - (Optional) The public certificate, in PEM format, that you received from your SSL certificate provider.


## Return Values

### Fn::GetAtt

`CaCertificate` - The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.

`CertificateName` - A friendly name for the certificate bundle. It must be unique and it cannot be changed. Valid certificate bundle names include only alphanumeric characters, dashes, and underscores. Certificate bundle names cannot contain spaces. Avoid entering confidential information.  Example: `example_certificate_bundle`.

`PublicCertificate` - The public certificate, in PEM format, that you received from your SSL certificate provider.

## See Also

* [oci_load_balancer_certificate](https://www.terraform.io/docs/providers/oci/r/load_balancer_certificate.html) in the _Terraform Provider Documentation_
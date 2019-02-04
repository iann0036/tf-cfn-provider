# Terraform::Google::ComputeSslCertificate

An SslCertificate resource, used for HTTPS load balancing. This resource
provides a mechanism to upload an SSL key and certificate to
the load balancer to serve secure connections from the user.


To get more information about SslCertificate, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=ssl_certificate_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Properties

`Project` - (Optional) The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

`NamePrefix` - (Optional) Creates a unique name beginning with the
specified prefix. Conflicts with `Name`.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_ssl_certificate](https://www.terraform.io/docs/providers/google/r/compute_ssl_certificate.html) in the _Terraform Provider Documentation_
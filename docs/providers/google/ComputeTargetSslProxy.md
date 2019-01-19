# Terraform::Google::ComputeTargetSslProxy

Represents a TargetSslProxy resource, which is used by one or more
global forwarding rule to route incoming SSL requests to a backend
service.


To get more information about TargetSslProxy, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/latest/targetSslProxies)
* How-to Guides
    * [Setting Up SSL proxy for Google Cloud Load Balancing](https://cloud.google.com/compute/docs/load-balancing/tcp-ssl/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_ssl_proxy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_target_ssl_proxy](https://www.terraform.io/docs/providers/google/r/compute_target_ssl_proxy.html) in the _Terraform Provider Documentation_
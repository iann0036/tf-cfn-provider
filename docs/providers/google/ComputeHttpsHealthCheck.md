# Terraform::Google::ComputeHttpsHealthCheck

An HttpsHealthCheck resource. This resource defines a template for how
individual VMs should be checked for health, via HTTPS.


~> **Note:** google_compute_https_health_check is a legacy health check.
The newer [google_compute_health_check](/docs/providers/google/r/compute_health_check.html)
should be preferred for all uses except
[Network Load Balancers](https://cloud.google.com/compute/docs/load-balancing/network/)
which still require the legacy version.


To get more information about HttpsHealthCheck, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/latest/httpsHealthChecks)
* How-to Guides
    * [Adding Health Checks](https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=https_health_check_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Properties

TBC

## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_https_health_check](https://www.terraform.io/docs/providers/google/r/compute_https_health_check.html) in the _Terraform Provider Documentation_
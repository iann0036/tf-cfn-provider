# Terraform::Google::ComputeBackendBucket

Backend buckets allow you to use Google Cloud Storage buckets with HTTP(S)
load balancing.

An HTTP(S) load balancer can direct traffic to specified URLs to a
backend bucket rather than a backend service. It can send requests for
static content to a Cloud Storage bucket and requests for dynamic content
a virtual machine instance.


To get more information about BackendBucket, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/latest/backendBuckets)
* How-to Guides
    * [Using a Cloud Storage bucket as a load balancer backend](https://cloud.google.com/compute/docs/load-balancing/http/backend-bucket)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=backend_bucket_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Properties

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_compute_backend_bucket](https://www.terraform.io/docs/providers/google/r/compute_backend_bucket.html) in the _Terraform Provider Documentation_
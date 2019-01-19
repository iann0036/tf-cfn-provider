# Terraform::Google::MonitoringAlertPolicy

A description of the conditions under which some aspect of your system is
considered to be "unhealthy" and the ways to notify people or services
about this state.


To get more information about AlertPolicy, see:

* [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/monitoring/alerts/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=monitoring_alert_policy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Properties

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.


## See Also

* [google_monitoring_alert_policy](https://www.terraform.io/docs/providers/google/r/monitoring_alert_policy.html) in the _Terraform Provider Documentation_
# Terraform::Google::PubsubTopic

A named resource to which messages are sent by publishers.


To get more information about Topic, see:

* [API documentation](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)
* How-to Guides
    * [Managing Topics](https://cloud.google.com/pubsub/docs/admin#managing_topics)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=pubsub_topic_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Properties

`Project` - (Optional) The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.


## See Also

* [google_pubsub_topic](https://www.terraform.io/docs/providers/google/r/pubsub_topic.html) in the _Terraform Provider Documentation_
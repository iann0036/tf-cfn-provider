# Terraform::Google::StorageDefaultObjectAccessControl

The DefaultObjectAccessControls resources represent the Access Control
Lists (ACLs) applied to a new object within a Google Cloud Storage bucket
when no ACL was provided for that object. ACLs let you specify who has
access to your bucket contents and to what extent.

There are two roles that can be assigned to an entity:

READERs can get an object, though the acl property will not be revealed.
OWNERs are READERs, and they can get the acl property, update an object,
and call all objectAccessControls methods on the object. The owner of an
object is always an OWNER.
For more information, see Access Control, with the caveat that this API
uses READER and OWNER instead of READ and FULL_CONTROL.


To get more information about DefaultObjectAccessControl, see:

* [API documentation](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/storage/docs/access-control/create-manage-lists)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=storage_default_object_access_control_public&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [google_storage_default_object_access_control](https://www.terraform.io/docs/providers/google/r/storage_default_object_access_control.html) in the _Terraform Provider Documentation_
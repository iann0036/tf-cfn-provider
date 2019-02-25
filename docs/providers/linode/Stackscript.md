# Terraform::Linode::Stackscript

Provides a Linode StackScript resource.  This can be used to create, modify, and delete Linode StackScripts.  StackScripts are private or public managed scripts which run within an instance during startup.  StackScripts can include variables whose values are specified when the Instance is created.  

For more information, see [Automate Deployment with StackScripts](https://www.linode.com/docs/platform/stackscripts/) and the [Linode APIv4 docs](https://developers.linode.com/api/v4#tag/StackScripts).

The Linode Guide, [Deploy a WordPress Site Using Terraform and Linode StackScripts](https://www.linode.com/docs/applications/configuration-management/deploy-a-wordpress-site-using-terraform-and-linode-stackscripts/), shows how a public StackScript can be used to provision a Linode Instance.   The guide, [Create a Terraform Module](https://www.linode.com/docs/applications/configuration-management/create-terraform-module/), demonstrates StackScript use through a wrapping module.

## Properties

`Label` - (Required) The StackScript's label is for display purposes only.

`Script` - (Required) The script to execute when provisioning a new Linode with this StackScript.

`Description` - (Required) A description for the StackScript.

`RevNote` - (Optional) This field allows you to add notes for the set of revisions made to this StackScript.

`IsPublic` - (Optional) This determines whether other users can use your StackScript. Once a StackScript is made public, it cannot be made private. *Changing `IsPublic` forces the creation of a new StackScript*.

`Images` - (Optional) An array of Image IDs representing the Images that this StackScript is compatible for deploying with.


## See Also

* [linode_stackscript](https://www.terraform.io/docs/providers/linode/r/stackscript.html) in the _Terraform Provider Documentation_
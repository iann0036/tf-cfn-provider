# Terraform::Gitlab::Label

This resource allows you to create and manage labels for your GitLab projects.
For further information on labels, consult the [gitlab
documentation](https://docs.gitlab.com/ee/user/project/labels.htm).

## Properties

`Project` - (Required) The name or id of the project to add the label to.

`Name` - (Required) The name of the label.

`Color` - (Required) The color of the label given in 6-digit hex notation with leading '#' sign (e.g. #FFAABB) or one of the [CSS color names](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords).

`Description` - (Optional) The description of the label.


## Return Values

### Fn::GetAtt

`Id` - The unique id assigned to the label by the GitLab server (the name of the label).

## See Also

* [gitlab_label](https://www.terraform.io/docs/providers/gitlab/r/label.html) in the _Terraform Provider Documentation_
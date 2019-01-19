# Terraform::Heroku::AddonAttachment

Attaches a Heroku Addon Resource to an additional Heroku App.

## Properties

`AppId` - (Required) The ID of the Heroku App to attach to.

`AddonId` - (Required) The ID of the existing Heroku Addon to attach.

`Name` - (Optional) A friendly name for the Heroku Addon Attachment.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the add-on attachment.

## See Also

* [heroku_addon_attachment](https://www.terraform.io/docs/providers/heroku/r/addon_attachment.html) in the _Terraform Provider Documentation_
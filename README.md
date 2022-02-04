# icinga2-gchat-notifications
Adds a notification command to send alerts via incoming webhook into Google Chat.

It is a modified version of plain old [mail-host-notification][1] and except curl, it doesn't need any external dependencies.

## Usage
- Copy included shell scripts to /etc/icinga2/scripts
- In Icinga (doesn't matter whether in Icingaweb2 or config files) clone notification command 'mail-host-notification' to 'gchat-host-notification' and 'mail-service-notification' to 'gchat-service-notification'.
- To both newly cloned commands, add a new argument: `-W` with value `$gchat_webhook_url$` with `required=true`.
- If done via Icingaweb2, add there a new mandatory field `gchat_webhook_url` and then the field will become visible in Custom properties. Paste your [webhook URL][2] there.
- If done via config files, just add `vars.gchat_webhook_url` with your [webhook URL][2] as it's value.
- Then, use the command in your [notification templates][3] as usual!

[1]: https://icinga.com/docs/icinga-2/latest/doc/03-monitoring-basics/#mail-host-notification
[2]: https://developers.google.com/chat/how-tos/webhooks
[3]: https://icinga.com/docs/icinga-2/latest/doc/03-monitoring-basics/#notifications

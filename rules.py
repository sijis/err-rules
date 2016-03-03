from datetime import datetime

from errbot import botcmd, BotPlugin


class Rules(BotPlugin):

    @botcmd
    def rules(self, msg, args):
        """Return a link to rules of the channel
            example:
            !rules
        """

        channel = msg.frm.channelname

        self.log.debug('{0} requested rules for {1}'.format(msg.frm, channel))
        default_response = 'I have no rules here.'

        response = self.get(channel, default_response)

        try:
            response = response.get('url')
        except AttributeError:
            pass

        self.send(
            msg.frm,
            response,
            message_type=msg.type,
            in_reply_to=msg,
            groupchat_nick_reply=True,
        )
        return

    @botcmd
    def rules_add(self, msg, args):
        """Add or updates a rule for a channel
            example:
            !rules add http://google.com
        """

        url = args
        if not url:
            self.send(
                msg.frm,
                'Forgot to add an url?',
                message_type=msg.type,
                in_reply_to=msg,
                groupchat_nick_reply=True,
            )
            return

        channel = msg.frm.channelname

        self[channel] = {
            'updated': datetime.now(),
            'url': url,
        }
        self.send(
            msg.frm,
            'Successfully added rule to channel.',
            message_type=msg.type,
            in_reply_to=msg,
            groupchat_nick_reply=True,
        )

    @botcmd
    def rules_delete(self, msg, args):
        """Delete rules from channel
            example:
            !rules delete
        """
        channel = msg.frm.channelname

        try:
            del self[channel]
            response = 'Successfully deleted rule.'
        except KeyError:
            response = 'I have no rules for this channel'

        self.send(
            msg.frm,
            response,
            message_type=msg.type,
            in_reply_to=msg,
            groupchat_nick_reply=True,
        )
        return

    @botcmd
    def rules_list(self, msg, args):
        """List channels that have rules defined
            example:
            !rules list
        """

        channels = self.keys()

        self.send(
            msg.frm,
            'Rules established in: {0}'.format(', '.join(channels)),
            message_type=msg.type,
            in_reply_to=msg,
            groupchat_nick_reply=True,
        )

import re
from errbot import BotPlugin, re_botcmd


class GuysWatch(BotPlugin):
    """What if we said "guys" less?"""

    @re_botcmd(pattern=r"(^| )guys( |$)", prefixed=False, flags=re.IGNORECASE)
    def watch_for_guys(self, msg, match):
        """If someone says "guys", errbot cringes"""
        return "Is gender important to understanding this?"

    @re_botcmd(pattern=r"(^| )blue jay( |$)", prefixed=False, flags=re.IGNORECASE)
    def watch_for_bluejay(self, msg, match):
        """Try adding a second function to this class"""
        return "Those are the screech-y ones, right?"

    @re_botcmd(pattern=r"(^| )test git( |$)", prefixed=False, flags=re.IGNORECASE)
    def watch_for_bluejay(self, msg, match):
        """Test updating a plugin via git repo"""
        return "If you're reading this, it's too git"
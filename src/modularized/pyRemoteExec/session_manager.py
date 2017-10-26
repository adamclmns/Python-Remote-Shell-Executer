"""
Create "Sessions" to be saved for multiple hosts. 
Sessions can be combined into SessionSets which will allow execution across many hosts. 
"""
# TODO: Sessions will be stored in .cfg file managed with ConfigManager
# TODO: Sessions will only be used for holding and passing Session information, not for logic


class Session():
    def __init__(self, *args, **kwargs):
        self._host
        self._user
        self._passwd
        self.friendlyName
    
    
class SessionSet():
    def __init__(self, *args, **kwargs):
        self.set = []
        self.friendlyName = None

    
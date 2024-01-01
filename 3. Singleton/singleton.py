class Singleton:
    class __impl:
        """Implementation of the singleton interface"""

        def spam(self):
            """Test method, return singleton id"""
            return id(self)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """Create singleton instance"""

        # check whether we already have an instance
        if Singleton.__instance is None:
            # create and remember instance
            Singleton.__instance = Singleton.__impl()

        # store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        """Delegate access to implementation"""
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """Delegate accesso to implementation"""
        return setattr(self.__instance, attr, value)


s1 = Singleton()
print(id(s1), s1.spam())

s2 = Singleton()
print(id(s2), s2.spam())

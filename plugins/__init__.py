class PluginException(Exception):
    """
    Base class for exceptions thrown by plugins.
    """


class PluginBase(object):
    """
    Base class for plugin implementation.

    To implement a plugin, create a file in the plugins directory
    called "mypluginname_plug.py". This file should implement
    plugin classes derived from the appropriate plugins base,
    e.g. for an import pluggin:

        import plugins

        class ImportPlugin(plugins.ImportPluginBase):
            # your implementation here
    """

    def __init__(self, tdb, tdenv):
        self.tdb = tdb
        self.tdenv = tdenv


class ImportPluginBase(PluginBase):
    """
    Base class for import plugins.

    When the user invokes the plugin, td will start by calling the
    "isExpectingData()" member function to determine if there is
    any expectation of new data. For instance, you might check to
    check the timestamp on a file in a dropbox folder.

    Next, prepareData() is called to fetch or load the data, which
    should return True if there is data to be processed, otherwise
    it should return False.

    Finally, in the case of prepareData() returning True, member
    function processData() is called to process the data.
    """

    defaultImportFile = "import.prices"

    def __init__(self, tdb, tdenv):
        super().__init__(tdb, tdenv)
        self.tdb = tdb
        self.tdenv = tdenv


    def isExpectingData(self):
        """
        Return False if there is definitely no new data,
        otherwise return True.
        """
        raise PluginException("Not implemented")


    def prepareData(self):
        """
        Plugin Must Implement:
        Prepare data for use - e.g. download from the web to
        a local file.
        Return True if there is data to be processed.
        """
        raise PluginException("Not implemented")


    def processData(self):
        """
        Plugin Must Implement:
        Handle the data that has been retrieved.
        """
        raise PluginException("Not implemented")


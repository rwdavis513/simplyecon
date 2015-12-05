__author__ = 'Bob Davis'


class APIBase(object):


    def call(self, *args, **kwargs):
        """
        Generic getter for creating the instance package to call the API
        :return: api results
        """
        raise NotImplementedError(
            '{} must implement _get_weather_info'.format(
                self.__class__.__name__))

    @property
    def URL(self):
        raise NotImplementedError(
            '{} must implement URL'.format(self.__class__.__name__))

    @property
    def URI(self):
        raise NotImplementedError(
                '{} must implement URI'.format(self.__class__.__name__))

    @property
    def params(self):
        raise NotImplementedError(
                '{} must implement params'.format(self.__class__.__name__))

    @property
    def key(self):
        raise NotImplementedError(
                '{} must implement API key'.format(self.__class__.__name__))

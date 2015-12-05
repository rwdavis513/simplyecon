__author__ = 'rwdavis513'

import requests
#from api_base import APIBase
#from exceptions import InitializationException
import pandas as pd

class APIBea(object):

    def __init__(self, key=None):
        self.URL = 'http://www.bea.gov'
        self.URI = '/api/data/'
        if not key:
            raise NotImplementedError('{} missing API key.'.format(self.__class__.__name__))
        else:
            self.key = key
            self.methods = ['GetDataSetList', 'GetParameterList',
                                     'GetParameterValues', 'GetParameterValuesFiltered']
            self.params = {'key':self.key, 'method':self.methods}
                    # Default method is set to getdatasetlist which is the highest level
                    # that displays which data sets are available

        self.results_format = "JSON"

    def build_API_URL_string(self,methodName,params = None):
        URL_string = self.URL + self.URI + "?&UserID=" + self.params['key'] + "&method=" + methodName
        if params and type(params) == dict:
            for k, v in params.iteritems():
                URL_string += "&" + k + "=" + v
        URL_string += "&ResultFormat="+self.results_format+"&"
        print(URL_string)
        return URL_string

    def call(self,methodName,params=None):
        url = self.build_API_URL_string(methodName,params)
        resp = requests.get(url)
        if resp.status_code == 200:
            try:
                respjson = resp.json()
            except ValueError:
                print("ValueError: JSON Object not found. Check if there is an internet sign on page for public wifi.")
        else:
            print('Response Error: ' + resp.status_code)
            raise
        return respjson

    def get_data_set_list(self):
        methodName = 'GETDATASETLIST'
        respjson = self.call(methodName)
        self.data_set_list = pd.DataFrame(respjson['BEAAPI']['Results']['Dataset'])
        return self.data_set_list

    def get_parameter_list(self,datasetname='RegionalData'):
        #http://www.bea.gov/api/data?&UserID={API KEY}&
        #    method=getparameterlist&datasetname=RegionalData&
        methodName = 'getparameterlist'
        params = {'datasetname':datasetname} ####
        #url = self.build_API_URL_string(methodName,params)
        respjson = self.call(methodName,params)
        self.param_list_df = pd.DataFrame(respjson['BEAAPI']['Results']['Parameter'])
        self.param_list_df['datasetname'] = params['datasetname']
        return self.param_list_df

    def get_parameter_values(self):
        #http://bea.gov/api/data?&UserID={{Your-API-Key}}&method=GetParameterValues
        #                        &datasetname=RegionalData&ParameterName=keycode&
        if not hasattr(self, 'param_list_df'):
            self.get_parameter_list()
        methodName='GetParameterValues'
        params = {'datasetname':self.param_list_df['datasetname'][0],   ####
                  'ParameterName':self.param_list_df['ParameterName'][0]} ####
        #url = self.build_API_URL_string(methodName,params)
        respjson = self.call(methodName,params)
        self.param_values = pd.DataFrame(respjson['BEAAPI']['Results']['ParamValue'])
        return self.param_values

    def get_data(self):
        #http://www.bea.gov/api/data?&UserID=Your-36CharacterKey&method=GetData&datasetname=RegionalData
        #                            &KeyCode=PCPI_CI&GeoFIPS=STATE&Year=2009&ResultFormat=JSON&
        # Need to loop through all parameters in param_list to include all the required ones. Or use GetParameterValuesFiltered

        if not hasattr(self,'param_values'):
            self.get_parameter_values()
        methodName = 'GetData'
        params = {'datasetname': self.param_list_df['datasetname'][0],
                  'KeyCode': self.param_values['KeyCode'][0]}
        respjson = self.call(methodName,params)
        self.statistic = respjson['BEAAPI']['Results']['Statistic']
        self.unit_of_measure = respjson['BEAAPI']['Results']['UnitOfMeasure']
        self.dimensions = pd.DataFrame(respjson['BEAAPI']['Results']['Dimensions'])
        self.data = pd.DataFrame(respjson['BEAAPI']['Results']['Data'])
        self.UTCProductionTime = respjson['BEAAPI']['Results']['UTCProductionTime']
        return self.data

if __name__ == "__main__":
    # simplyeconinfo@gmail.com
    key = 'E2CFAE73-FD09-45CD-B52E-2B5A0D1C4084'
    api = APIBea(key)
    #data_set_list = api.get_data_set_list()
    #print(data_set_list)
    data = api.get_data()
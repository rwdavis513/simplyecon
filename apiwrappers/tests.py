__author__ = 'rwdavis513'


from api_bea import APIBea
import pandas as pd

def test_parameter_values():

    respjson = {u'BEAAPI': {u'Request': {u'RequestParam': [{u'ParameterName': u'DATASETNAME', u'ParameterValue': u'REGIONALDATA'}, {u'ParameterName': u'RESULTFORMAT', u'ParameterValue': u'JSON'}, {u'ParameterName': u'USERID', u'ParameterValue': u'E2CFAE73-FD09-45CD-B52E-2B5A0D1C4084'}, {u'ParameterName': u'METHOD', u'ParameterValue': u'GETPARAMETERLIST'}]}, u'Results': {u'Parameter': [{u'MultipleAcceptedFlag': u'0', u'ParameterDataType': u'string', u'ParameterIsRequiredFlag': u'1', u'AllValue': u'', u'ParameterDescription': u'The code of the key statistic requested', u'ParameterDefaultValue': u'', u'ParameterName': u'KeyCode'}, {u'MultipleAcceptedFlag': u'1', u'ParameterDataType': u'string', u'ParameterIsRequiredFlag': u'0', u'AllValue': u'', u'ParameterDescription': u'GeoFips Code', u'ParameterDefaultValue': u'', u'ParameterName': u'GeoFips'}, {u'MultipleAcceptedFlag': u'1', u'ParameterDataType': u'integer', u'ParameterIsRequiredFlag': u'0', u'AllValue': u'ALL', u'ParameterDescription': u'Year', u'ParameterDefaultValue': u'ALL', u'ParameterName': u'Year'}]}}}
    parameter_list_df = pd.DataFrame(respjson['BEAAPI']['Results']['Parameter'])
    parameter_list_df['datasetname'] = 'RegionalData'
    api = APIBea('INSERTAPIKEYHERE')
    print(api.get_parameter_values(parameter_list_df))

test_parameter_values()
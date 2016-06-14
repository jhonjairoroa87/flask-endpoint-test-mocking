import json
import mock
import unittest
import types

from app import flask_app


class TestViews(unittest.TestCase):
    """
    Tests of the project endpoints
    """

    # An example of the values the /get_groups endpoint is supposed to return
    _get_all_groups_mock_return = [{
        "city": "Medellin",
        "country_code": "CO",
        "country_name": "Colombia",
        "members": 848,
        "name": "Medellin Python y Django Meetup"
    }]

    @classmethod
    def setUpClass(self):
        self.app = flask_app.test_client()

    def get_index_test(self):
        """
        Validate the values returned by the / endpoint
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @mock.patch('utils.meetup_utils.MeetupUtils.get_all_groups', return_value=_get_all_groups_mock_return)
    def get_groups_test(self, get_all_groups_mock):
        """
        Validate the values returned by the /get_groups endpoint
        """
        response = self.app.get('/get_groups')

        # validates the response status code is 200 OK
        self.assertEqual(response.status_code, 200, "the response status code should be 200")

        # validates the rerponse data string length is greater that 0
        self.assertTrue(len(response.data) > 0, "the response data string lenght should be  greater than 0")

        # validate that the response.data string can be converted to json
        response_dict = {}
        try:
            response_dict = json.loads(response.data)
        except Exception:
            self.assertTrue(False, "the response.dict string cannot be parsed to a json object")

        # Validate the response dict contains a 'result' key
        self.assertTrue('result' in response_dict, "the response dict should contain a 'result' key ")

        # validate the group list length is greater that cero
        group_list = response_dict['result']
        self.assertTrue(len(group_list) > 0, "the group list should be greater than 0")

        group_fields = {
            "city": types.UnicodeType,
            "country_code": types.UnicodeType,
            "country_name": types.UnicodeType,
            "members": types.IntType,
            "name": types.UnicodeType
        }

        for group_element in group_list:
            for group_field_name, group_field_type in group_fields.iteritems():

                # validate each group is type Dict
                self.assertEqual(type(group_element), types.DictType, "the group element should be a dict")

                # validate that each group contains the expected fields
                self.assertTrue(group_field_name in group_element, "the group element should have a '%s' key" %
                                group_field_name)

                # validate the type of each attribute of each group
                self.assertEqual(type(group_element[group_field_name]), group_fields[group_field_name],
                                 "the group element type should be '%s'" % group_fields[group_field_name])

     @mock.patch('utils.meetup_utils.MeetupUtils.get_all_groups', return_value=_get_all_groups_mock_return)
    def get_groups_test(self, get_all_groups_mock):
        """
        Validate the values returned by the /get_groups endpoint
        """
        response = self.app.get('/get_groups')

        # validates the response status code is 200 OK
        self.assertEqual(response.status_code, 200, "the response status code should be 200")

        # validates the rerponse data string length is greater that 0
        self.assertTrue(len(response.data) > 0, "the response data string lenght should be  greater than 0")

        # validate that the response.data string can be converted to json
        response_dict = {}
        try:
            response_dict = json.loads(response.data)
        except Exception:
            self.assertTrue(False, "the response.dict string cannot be parsed to a json object")

        # Validate the response dict contains a 'result' key
        self.assertTrue('result' in response_dict, "the response dict should contain a 'result' key ")

        # validate the group list length is greater that cero
        group_list = response_dict['result']
        self.assertTrue(len(group_list) > 0, "the group list should be greater than 0")

        group_fields = {
            "city": types.UnicodeType,
            "country_code": types.UnicodeType,
            "country_name": types.UnicodeType,
            "members": types.IntType,
            "name": types.UnicodeType
        }

        for group_element in group_list:
            for group_field_name, group_field_type in group_fields.iteritems():

                # validate each group is type Dict
                self.assertEqual(type(group_element), types.DictType, "the group element should be a dict")

                # validate that each group contains the expected fields
                self.assertTrue(group_field_name in group_element, "the group element should have a '%s' key" %
                                group_field_name)

                # validate the type of each attribute of each group
                self.assertEqual(type(group_element[group_field_name]), group_fields[group_field_name],
                                 "the group element type should be '%s'" % group_fields[group_field_name])

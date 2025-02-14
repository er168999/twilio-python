# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TaskQueueBulkRealTimeStatisticsTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .bulk_real_time_statistics.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TaskQueues/RealTimeStatistics',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/RealTimeStatistics",
                "task_queue_data": {
                    "total_eligible_workers": 100,
                    "activity_statistics": [
                        {
                            "friendly_name": "Idle",
                            "workers": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        },
                        {
                            "friendly_name": "Busy",
                            "workers": 9,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        },
                        {
                            "friendly_name": "Offline",
                            "workers": 6,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        },
                        {
                            "friendly_name": "Reserved",
                            "workers": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        }
                    ]
                },
                "task_queue_response_count": 100
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .bulk_real_time_statistics.create()

        self.assertIsNotNone(actual)

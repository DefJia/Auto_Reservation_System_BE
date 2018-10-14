from datetime import datetime
import time


class Time:
    @staticmethod
    def wait_until(time_):
        """
        It needs to be clarified that the time is that on remote server.
        :return: 0 -> time is up
        """

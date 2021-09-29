# @Time    : 
# @Author  : chen
import unittest
from datetime import datetime, timedelta, timezone
class TestDatetime(unittest.TestCase):
    def test_get_datetime(self):
        """指定日期和时间datetime"""
        expected = "2017-02-22 16:05:26"
        actual = datetime(2017, 2, 22, 16, 5, 26)
        # print(actual)
        self.assertEqual(expected, str(actual))

    def test_datetime_translation_timestamp(self):
        """将datetime转化成timestamp,返回的是秒"""
        expected = 1487750726.0
        actual = datetime(2017, 2, 22, 16, 5, 26).timestamp()
        # print(type(actual))
        self.assertEqual(expected, actual)

    def test_timestamp_translation_datetime(self):
        """将timestamp转化成datetime格式"""
        expected = "2017-02-22 16:05:26"
        actual = datetime.fromtimestamp(1487750726.0)
        # print(actual)
        self.assertEqual(expected, str(actual))

    def test_str_translation_datetime(self):
        """将str转化成datetime格式"""
        expected = datetime(2017, 2, 22, 16, 5, 26)
        actual = datetime.strptime('2017-02-22 16:05:26', '%Y-%m-%d %H:%M:%S')
        # print(actual)
        self.assertEqual(expected, actual)

    def test_datetime_translation_str(self):
        """将datetime转化成str"""
        excepted = '2017-02-22 16:05:26'
        actual = datetime(2017, 2, 22, 16, 5, 26).strftime('%Y-%m-%d %H:%M:%S')
        # print(type(actual))
        self.assertEqual(excepted, actual)

    def test_datetime_add(self):
        """利用timedelta进行时间相加"""
        # 加1小时
        excepted1 = datetime.strptime('2017-02-22 17:05:26', '%Y-%m-%d %H:%M:%S')
        actual1 = datetime.strptime('2017-02-22 16:05:26', '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)
        # 加2天，10小时
        excepted2 = datetime.strptime('2017-02-25 02:05:26', '%Y-%m-%d %H:%M:%S')
        actual2 = datetime.strptime('2017-02-22 16:05:26', '%Y-%m-%d %H:%M:%S') + timedelta(hours=10, days=2)

        self.assertEqual(excepted1, actual1)
        self.assertEqual(excepted2, actual2)

    def test_datetime_plus(self):
        """利用timedelta进行时间相减"""
        # 减1小时
        excepted1 = datetime.strptime('2017-02-22 16:05:26', '%Y-%m-%d %H:%M:%S')
        actual1 = datetime.strptime('2017-02-22 17:05:26', '%Y-%m-%d %H:%M:%S') - timedelta(hours=1)
        self.assertEqual(excepted1, actual1)

    def test_timezone_translation(self):
        """转换时区"""
        utc_datetime = datetime.strptime('2017-02-22 17:05:26', '%Y-%m-%d %H:%M:%S').replace(
            tzinfo=timezone(timedelta(hours=8)))
        # 北京时间
        bj_datetime = utc_datetime.astimezone(timezone(timedelta(hours=8)))
        # 东京时间
        dj_datetime = bj_datetime.astimezone(timezone(timedelta(hours=9)))
        # print(dj_datetime)
        self.assertEqual((bj_datetime + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S'),
                         dj_datetime.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    unittest.main()
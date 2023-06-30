import unittest
from src.main.delegators.delegator_types import DelegatorTypes
import src.main.main as main
import src.main.configurations

class MainTest(unittest.TestCase):    
    TEST_JSON_URI = 'configurations_test.json'

    def test_configs(self) -> map:
        return main.get_configs(self.TEST_JSON_URI)


    def test_get_configs(self):
        configs = self.test_configs()
        assert configs
        assert configs["reddit"]
        assert configs["reddit"]["username"]
        assert configs["reddit"]["password"]
        assert configs["reddit"]["client_id"]
        assert configs["reddit"]["client_pw"]
        assert configs["reddit"]["user_agent"]
        assert configs["reddit"]["subreddits"]
        assert configs["spreadsheet"]
        assert configs["spreadsheet"]["username"]
        assert configs["spreadsheet"]["password"]
        assert configs["spreadsheet"]["url"]


    def test_get_delegator_config_key_missing(self):
        configs = self.test_configs()
        '''
        def testListSlicing(self):
            with self.assertRaises(TypeError) as ctx:
                self.testListNone[:1]
            self.assertEqual("'NoneType' object is not subscriptable", str(ctx.exception))
        '''
        with self.assertRaises(ValueError) as err:
            main.get_delegator(configs, "BAD KEY")
        self.assertEqual("Configs provided are missing values for 'BAD KEY'.", str(err.exception))

    def test_get_reddit(self):
        configs = self.test_configs()
        reddit = main.get_reddit_delegator(configs)
        assert reddit

    
    def test_get_ssd(self):
        configs = self.test_configs()
        ssd = main.get_ssd_delegator(configs)
        assert ssd
        

    def test_build_bot(self):
        reddit, ssd = main.get_delegators(self.TEST_JSON_URI)
        assert reddit
        assert ssd


if __name__ == '__main__':
    unittest.main()
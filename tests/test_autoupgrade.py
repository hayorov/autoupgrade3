from unittest import TestCase

from autoupgrade3 import normalize_version, AutoUpgrade
#import sys


#print sys.argv
#autoupgrade3.AutoUpgrade("x").restart()

#autoupgrade3.AutoUpgrade("pip").upgrade_if_needed()

#autoupgrade3.AutoUpgrade("alsdhf").upgrade()
#autoupgrade3.AutoUpgrade("pip").upgrade()

class TestFunctions(TestCase):
    
    def test_normalize(self):
        self.assertGreater(normalize_version('0.1.2'), normalize_version('0.1.1'))
        self.assertGreater(normalize_version('0.1.5A'), normalize_version('0.1.5'))
        self.assertGreater(normalize_version('0.10.0'), normalize_version('0.9.5'))
        self.assertGreater(normalize_version('1.2.3'), normalize_version('1.2'))
        self.assertGreater(normalize_version('1.2A.3'), normalize_version('1.2.3'))
        self.assertEqual(normalize_version('1.2.3'), normalize_version('1.2.3'))
        
    def test_upgrade_default(self):
        bs = AutoUpgrade("beautifulsoup4", verbose = True)
        bs.upgrade_if_needed(False)
        
    def test_upgrade_index(self):
        bs = AutoUpgrade("beautifulsoup4", "https://pypi.python.org/simple", verbose = True)
        bs.upgrade_if_needed(False)

#  This file is part of Headphones.
#
#  Headphones is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Headphones is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Headphones.  If not, see <http://www.gnu.org/licenses/>.


import unittest
from headphones.postprocessor import find_in_path


class PostProcessorTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_in_path(self):
        result = find_in_path("tests/resources")[:6]
        expected = ['tests/resources/unparseable.alac.m4a',
                    'tests/resources/t_time.m4a',
                    'tests/resources/space_time.mp3',
                    'tests/resources/partial.flac',
                    'tests/resources/empty.ape',
                    'tests/resources/full.ape']
        self.assertEqual(result, expected)
        result = find_in_path("-----")
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()

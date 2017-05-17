from unittest import TestCase


class TestPrint_binary(TestCase):
    def test_print_binary(self):
        try:
            from build import print_binary
        except ImportError:
            self.assertFalse("No function found")

        self.assertEqual(print_binary(None), 'ERROR')
        self.assertEqual(print_binary(0), 'ERROR')
        self.assertEqual(print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        self.assertEqual(print_binary(num), expected)
        num = 0.987654321
        self.assertEqual(print_binary(num), 'ERROR')

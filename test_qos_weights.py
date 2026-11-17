import unittest
from qos_weights import normalize_weights

class WeightTests(unittest.TestCase):
    def test_ratios_are_preserved(self):
        self.assertEqual(normalize_weights(2, 3, 5), (0.2, 0.3, 0.5))

    def test_zero_sum_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_weights(0, 0, 0)

    def test_negative_and_nonfinite_inputs_are_rejected(self):
        for value in (-1, float('inf'), float('-inf'), float('nan')):
            with self.subTest(value=value), self.assertRaises(ValueError):
                normalize_weights(value, 1, 1)

    def test_single_objective(self):
        self.assertEqual(normalize_weights(0, 2, 0), (0, 1, 0))

    def test_large_finite_weights_do_not_overflow(self):
        result = normalize_weights(1e308, 1e308, 1e308)
        self.assertAlmostEqual(sum(result), 1)
        self.assertTrue(all(value > 0 for value in result))

if __name__ == '__main__':
    unittest.main()

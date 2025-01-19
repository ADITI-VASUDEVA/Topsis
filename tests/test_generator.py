import unittest
from dynamic_invoice.generator import generate_invoice

class TestInvoiceGenerator(unittest.TestCase):
    def test_generate_invoice(self):
        
        try:
            generate_invoice()
        except Exception as e:
            self.fail(f"generate_invoice raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

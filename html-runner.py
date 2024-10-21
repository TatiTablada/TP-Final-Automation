import unittest
from HtmlTestRunner import HTMLTestRunner

test_suite = unittest.TestLoader().discover('tests')
runner = HTMLTestRunner(output='test-reports', report_title='Reporte de pruebas', combine_reports = True)
try:
    runner.run(test_suite)
except:
    print('Hubo un error')

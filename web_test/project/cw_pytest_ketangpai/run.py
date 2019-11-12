import pytest

if __name__ == "__main__":
    pytest.main([
        "-m join",
        "-s",
        "--resultlog=report/test_report.txt",
        "--junitxml=report/test_report.xml",
        "--html=report/test_report.html",
        "--alluredir=report/allure_data/"
    ])
# join or enter or

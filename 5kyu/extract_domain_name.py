# Instructions:
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"


# My Solution
def domain_name(url):
    url = url.split("//")
    if len(url) > 1:
        url = url[1]
    else:
        url = url[0]
    url = url.split(".")
    return url[1] if url[0] == "www" else url[0]


# Sample Tests
Test.assert_equals(domain_name("http://google.com"), "google")
Test.assert_equals(domain_name("http://google.co.jp"), "google")
Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
Test.assert_equals(domain_name("https://youtube.com"), "youtube")


# Top Answer
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
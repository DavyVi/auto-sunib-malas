# Auto Sunib AWS Activity Filler
1. Change the Activity and Description variable to your liking
2. ~~Change the SSOURL to your account SSO URL (Video Tutorial: https://youtu.be/9Y_jvlgc7jY)~~
3. The SSO login token is now protected by Azure auth, so we need to login to the enrichment app (either via Selenium automated login (Sometimes if a process fails, just rerun the code cell, this caused by the page is haven't loaded properly yet the driver already input the clicks) or manually login after the browser is popped up by the webdriver) then get the cookie to send the payload via API.
4. Run The Program
5. Don't Forget to Submit Your Log Book by opening the website

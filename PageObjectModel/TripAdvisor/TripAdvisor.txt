I'm using Page Object Model (POM) design pattern to create Object Repository for the web UI elements. 
For each web page in the application, there is a corresponding page class.
The Page class will find the WebElements of that web page.
It contains page methods which perform operations on those WebElements. 

I created 2 page classes:
1) Verifying the login functionality of the website.
2) Verifying the functionality of "Save my trips" feature.

I also created a test suite that runs both page classes.


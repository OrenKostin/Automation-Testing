I'm using Page Object Model (POM) design pattern to create Object Repository for the web UI elements. 
For each web page in the application, there is a corresponding page class.
The Page class will find the WebElements of that web page.
It contains page methods which perform operations on those WebElements. 

I created 2 page classes:
1) Automating the login functionality of the website
2) Automating the purchase process of the "Lego Star Wars" brand.

I created the scripts using Data-driven Testing (DDT).
The test data is read from data files (CSV files), instead of using the same hard-coded values each time the test runs. 
DDT gives more flexibility, by testing how the application handles various inputs effectively. 

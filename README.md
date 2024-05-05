<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 3

Conversion time: 0.702 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Mon Mar 18 2024 18:17:14 GMT-0700 (PDT)
* Source doc: Custom-LLM Readme
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->

This project allows non-technical users to query a database using plain-text and get a visual representation of the data. For example, business analysts may want to compare the revenue and operating costs of various services. Despite not knowing the database structure, they can simply enter a query (ex. "Give me a bar graph comparison for the revenue and operating costs of our services") and get a bar graph with all the necessary details. 

This is accomplished by using Langchain to seamlessly integrate database queries, LLM models, and API calls. Furthermore, it uses Program-Aided Language Models - an approach that encourages LLMs to solve problems through generating code. This approach has a higher accuracy compared to conventional approaches for prompts that involve reasoning. 

The following are examples of the visuals that can be generated from plain-text queries. These examples come from a PostgreSQL database containing weather data for Canadian provinces and territories. 

```
“can i get a scatter plot of the low and high temperatures over time (months) in toronto and vancouver”
```
![image](https://github.com/David-Ykz/custom-llm/assets/59211419/fd9c3538-b774-4e93-9f67-30987853adbd)

```
“can i get a line graph of the daylight hours for each of the different regions per month”
```
![image](https://github.com/David-Ykz/custom-llm/assets/59211419/62c427b3-55f7-4d65-8898-56e12d145f51)

```
“can i get a correlation between the hours of daylight and the amount of rainfall”
```
![image](https://github.com/David-Ykz/custom-llm/assets/59211419/4e1debe7-b886-4eb1-b1b6-fdb210736538)

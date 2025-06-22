# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: GOWTHAM N

*INTERN ID*: CT04DF178

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

*DESCRIPTION*:

        For Task 1 of the CodTech Python Internship, I was required to develop a Python-based project that fetches real-time data from a public API and visualizes the results using appropriate libraries. This task served as an excellent opportunity to gain hands-on experience with API integration, data preprocessing, and interactive visualization — three essential skills in data science and modern software development. I chose to work with a COVID-19 statistics API provided by Rootnet, which supplies live data about the pandemic’s impact across various Indian states and union territories. The objective was to build a clean, interactive, and informative dashboard that could help users easily understand the regional distribution and intensity of COVID-19 cases in India.To begin the project, I used the `requests` library to send an HTTP GET request to the API endpoint. Once the data was successfully fetched, I parsed the JSON response to extract the relevant portion, specifically the “regional” section which contained state-wise data. This information was then converted into a structured format using a `pandas` DataFrame for easier manipulation and analysis. I renamed the column headers to more descriptive terms such as “State”, “Total Cases”, “Recovered”, and “Deaths” to make the dataset more readable and meaningful. I also sorted the data in descending order based on the number of total confirmed cases and extracted the top 10 most affected states for focused visualization. After preparing the dataset, I used the `plotly` library to construct an interactive dashboard. Instead of relying on static libraries like Matplotlib or Seaborn, I chose Plotly due to its rich interactivity, hover tooltips, and flexible layout options. Using `plotly.subplots.make_subplots`, I created a 3-row by 2-column grid layout where each subplot showcased a different aspect of the dataset. The first chart was a bar graph showing the total number of COVID-19 cases in each state, making it easy to compare the scale of the outbreak across regions. The second chart was a pie chart representing the percentage contribution of the top 10 states in total case count, which visually highlighted the regions that were most severely affected.

The third visualization was a box plot that provided statistical insights into the spread of total cases, recoveries, and deaths. It helped illustrate the variance and distribution within these key metrics. The fourth chart, a histogram, displayed how case numbers were distributed among states — showing whether cases were concentrated in a few areas or more evenly spread. The fifth and final chart was a line graph showing trends of total confirmed cases across states, offering a continuous visual representation of the data. To enhance readability and aesthetics, I applied consistent formatting throughout the dashboard. I used the "Times New Roman" font, set appropriate font sizes and colors, and centered the main title which read “COVID-19 Dashboard for India”. The subplot titles and annotations were styled to match the overall theme, and the layout spacing was carefully adjusted to prevent visual clutter. I also removed unnecessary legends to maintain simplicity and allow users to focus on the key visual elements.

#OUTPUT

https://github.com/GowthamN-1806/API-INTEGRATION-AND-DATA-VISUALIZATION/issues/1#issue-3166076838

In conclusion, Task 1 enabled me to apply core programming and data visualization skills to a real-world problem. I gained practical experience in working with web APIs, handling and cleaning JSON data, transforming it using pandas, and representing it interactively with Plotly. This project not only strengthened my technical foundation but also helped me understand how to build data-driven applications that provide clear, accessible insights to end-users. By the end of the task, I was able to deliver a polished, informative, and interactive dashboard that showcased the regional impact of COVID-19 in India in a visually compelling manner, fulfilling the task requirements effectively.



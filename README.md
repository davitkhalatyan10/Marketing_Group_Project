DS223-Marketing-Analytics-Group-Project-Group2
# Customer Analysis 

# Overview
The Customer Frequency Analysis Python Package is designed to help businesses analyze customer behavior and purchasing patterns. By leveraging transaction data, businesses can gain insights into customer frequency, preferences, and spending habits. This information is invaluable for making data-driven decisions and implementing strategies to improve customer retention and overall business performance. 

# Problem
Many businesses struggle to understand their customers' behavior and preferences, leading to ineffective marketing campaigns, suboptimal product offerings, and decreased customer satisfaction. Without insights into customer frequency and purchasing patterns, businesses may miss opportunities to enhance customer relationships and drive revenue growth. 
Customer retention is a pervasive challenge encountered by businesses across diverse industries. In an era marked by evolving consumer preferences and intensified market competition, understanding why customers decrease their engagement or discontinue interactions is paramount. This necessitates a deep dive into transactional data to uncover trends and behaviors indicative of waning customer loyalty. The objective is to glean insights into customer preferences, purchase patterns, and satisfaction levels, facilitating the formulation of tailored retention strategies. Addressing this challenge entails adopting a comprehensive approach to customer relationship management, characterized by personalized experiences and targeted marketing initiatives designed to meet the unique needs of individual customers, regardless of the industry they operate in.

# Solution 
The Customer Frequency Analysis Python Package provides a comprehensive toolkit for businesses to conduct customer frequency analysis. By analyzing transaction data, businesses can identify patterns and trends in customer behavior, segment customers based on their transaction history, and visualize insights to inform decision-making.
The Customer Frequency Analysis Python Package offers a comprehensive toolkit tailored for businesses seeking to delve deep into their customer data. Leveraging transaction records, the package enables businesses to uncover intricate patterns and trends in customer behavior, essential for informed decision-making and strategic planning. With a focus on customer retention and satisfaction, the package provides advanced segmentation techniques to categorize customers into distinct groups based on their transaction history, preferences, and engagement levels. Additionally, the package incorporates two primary case scenarios: RFM (Recency, Frequency, Monetary) analysis and segmentation analysis.

**Case Scenario 1**

*Restaurant Marketing Strategy*

# Scenario: A restaurant aims to enhance customer engagement and drive repeat business.

Use of Customer Frequency Analysis: By analyzing customer frequency, the restaurant can identify its most loyal customers and understand their preferences better. For example, they can determine which dishes or promotions attract customers back more frequently. With this insight, they can create targeted marketing campaigns or loyalty rewards that appeal to specific customer segments. Additionally, they can identify customers who haven't visited in a while and offer them incentives to return, such as discounts or special events. Customer frequency analysis guides the restaurant in crafting personalized experiences and communication strategies to increase customer retention and overall satisfaction.

**Case Scenario 2**

*Online Marketplace Customer Engagement*

# Scenario: An online marketplace wants to improve customer engagement and increase repeat purchases.
Use of Customer Frequency Analysis: By analyzing how often customers make purchases on the platform, the marketplace can identify segments of users with varying levels of engagement. For example, they may find that certain customers make frequent purchases while others only buy occasionally. With this insight, the marketplace can personalize product recommendations, email campaigns, and promotions based on each customer's buying frequency. They can also identify trends such as seasonal fluctuations or specific product preferences among high-frequency purchasers and tailor their marketing strategies accordingly. Additionally, they can experiment with loyalty programs or subscription options to incentivize more frequent purchases. Customer frequency analysis helps the online marketplace understand customer behavior and implement targeted strategies to increase engagement and drive sales.

# Result
With the Customer Frequency Analysis Python Package, businesses can:

*     Gain insights into customer frequency, recency, and monetary value

*     Segment customers into different groups based on transaction behavior

*      Target specific customer segments with personalized marketing strategies

*      Optimize product offerings and pricing strategies to meet customer needs

*     Enhance customer satisfaction and drive repeat business

# Features
*        Data Management: Store and retrieve transaction data in a centralized database

*     Frequency Analysis: Identify patterns in customer behavior, such as purchase frequency and recency

*     Segmentation: Segment customers into different groups based on transaction history

*       Visualization: Create charts, graphs, and reports to visualize customer behavior trends

*      API Integration: Integrate with existing systems and workflows using the provided API

# Usage

**Installation**

1.      Clone the repository: git clone [repository-url]
2.      Navigate to the project directory: cd [project-directory]
3.      Install dependencies: pip install -r requirements.txt


**Setting Up the Database**

   *Run the setup.py script to set up the initial database and environment.*
   
   *Run this line to install our package:*
```
pip install CustomerFrequency

```

**Data Generation**

Run the file data_generator.ipynb

**SQL Connection**

Establish a SQL connection and execute a query to retrieve transaction data 

**FastAPI Integration**

Run the file **run.py** for connecting to API.
After these steps copy the host link and paste it in the search bar adding "docs" after it. There are different functionalities in the FASTAPI page. We can get average frequency, top customers, transactions, also we can create, update or delete the data. 

**MkDocs**

[Mkdocs File](http://127.0.0.1:8000/)

**API calls**

•       [DELETE](http://localhost:8000/docs#/default/coffee_transaction_create_data_coffee_purchase_post)

•       [PUT](http://localhost:8000/docs#/default/update_item_update_data__item_id__put)

•       [POST](http://localhost:8000/docs#/default/create_item_create_data_post)

• [AVGFREQUENCY](http://localhost:8000/docs#/default/reach_lowest_average_visit_frequency_get_data_avg_frequency_get) 

• [CUSTOMERSEGMENTATIONPLOT](http://localhost:8000/docs#/default/get_customer_segments_plot_get_customer_segments_plot_get)

• [GETBOXPLOT](http://localhost:8000/docs#/default/get_boxplot_get_boxplot_get)

• [GETSCATTERPLOT](http://localhost:8000/docs#/default/get_scatter_plot_get_scatter_plot_get)

• [GETTOPCUSTOMERS](http://localhost:8000/docs#/default/appreciate_top_visits_get_data_top_customers_get)

• [GETBESTSELLERNOTIFICATION](http://localhost:8000/docs#/default/bestseller_notification_get_data_bestseller_get)



**PyPiLink**

[PyPiLink](https://pypi.org/manage/project/customerfrequency/releases/)



**Members:**

- Mane Stepanyan
- Elina Davtyan
- Davit Khalatyan
- Davit Ohanjanyan
- Vram Papyan

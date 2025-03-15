# Customer Purchase Analytics Pipeline

## Executive Summary
The Customer Purchase Analytics Pipeline is an enterprise-grade solution engineered to ingest, transform, and visualize customer transaction data. By integrating Apache Airflow, Azure Databricks, Azure SQL Database, and interactive dashboards in Power BI and Tableau, this pipeline empowers data-driven decisions and maximizes business impact.

## Architecture Overview
- **Data Ingestion:** Azure Databricks ingests raw transaction data from Azure Data Lake.
- **Data Transformation:** PySpark cleans and aggregates data, computing key performance metrics.
- **Data Storage:** Processed data is securely stored in an Azure SQL Database.
- **Dashboarding:** Live dashboards are built in Power BI and Tableau, providing real-time analytics through direct connections to the SQL Database.
- **Orchestration:** Apache Airflow automates the ETL process, ensuring reliability and timely updates.

## Key Features
- **Automated ETL:** Robust, scheduled data workflows with Apache Airflow.
- **Scalable Processing:** High-performance data processing using Azure Databricks and PySpark.
- **Secure Data Management:** Best-in-class security and compliance with Azure SQL Database.
- **Interactive Dashboards:** Industry-leading visualization using Power BI and Tableau.
- **CI/CD Ready:** Seamless integration with modern CI/CD pipelines for continuous improvement.
- **Enterprise Quality:** Modular design, extensive data quality checks, and end-to-end audit trails.


## Setup & Deployment
1. **Airflow:**  
   Configure your Airflow environment with the required environment variables and deploy the DAG from the `airflow` folder.

2. **Azure Databricks:**  
   Import notebooks from the `databricks_notebooks` folder into your Databricks workspace. Ensure connections to Azure Data Lake and the SQL Database are configured.

3. **Azure SQL Database:**  
   Run the scripts in the `sql_queries` folder to create tables and execute data quality checks.

4. **Dashboard Integration:**  
   Leverage the provided Power BI (`Customer_Purchase.pbix`) and Tableau (`Customer_Purchase.twb`) files to connect directly to the Azure SQL Database and create interactive dashboards. These dashboards offer dynamic visualizations of total sales trends, customer segmentation, and transaction analytics.

5. **CI/CD:**  
   Integrate GitHub Actions or Azure Pipelines to automate testing, deployment, and monitoring of the entire pipeline.

## Business Impact
- **Actionable Insights:** Deliver real-time analytics to empower strategic decisions.
- **Operational Excellence:** Streamline data workflows to reduce manual intervention and improve efficiency.
- **Customer Engagement:** Uncover trends and insights to enhance customer experience and drive revenue growth.

## Security & Compliance
- Secure credential management with environment variables and Azure Key Vault.
- Data encryption in transit and at rest.
- Compliance with industry-standard data privacy regulations.

## Get In Touch
For more information, collaborations, or inquiries, please contact us at [habibagrebi7@gmail.com](mailto:habibagrebi7@gmail.com) or connect on [LinkedIn]([https://www.linkedin.com](https://www.linkedin.com/in/agrebi-mohamed-habib-4b767b13b/)).

## License
This project is licensed under the MIT License.

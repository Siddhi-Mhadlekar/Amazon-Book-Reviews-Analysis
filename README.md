# Amazon Book Reviews Analysis

## Overview
This project aims to securely manage, streamline, and perform analysis on structured Amazon book reviews data based on various metrics.
The architecture includes data ingestion with AWS Lambda, ETL processing with AWS Glue, storage in Amazon S3, querying with AWS Athena, and visualization with Amazon QuickSight.

## Project Goals
- **Data Ingestion**: Build a mechanism to ingest data from different sources.
- **ETL System**: Transform raw data into the proper format.
- **Data Lake**: Centralized repository to store data from multiple sources.
- **Scalability**: Ensure the system scales as the data size increases.
- **Cloud**: Use AWS for processing vast amounts of data.
- **Reporting**: Build a dashboard to get insights from the data.

## Services Used
1. Amazon S3: Store all raw and processed data in a centralized data lake for scalable access and analysis.
2. AWS IAM: Manage secure access and permissions for resources like S3 buckets, Glue jobs, and Lambda functions.
3. Amazon QuickSight: Create interactive dashboards and reports to visualize insights from the data.
4. AWS Glue: Transform raw data into structured formats and catalog data for efficient ETL processing.
5. AWS Lambda: Automate data ingestion and processing by triggering functions in response to events like new data arrival.
6. AWS Athena: Run SQL queries directly on data in S3 to perform ad-hoc analysis and generate insights efficiently.


## Dataset
Dataset on Amazon's Top 50 bestselling books from 2009 to 2019. Contains 550 books, data has been categorized into fiction and non-fiction using Goodreads
I'm using a publicly available Amazon book reviews dataset. [Download the dataset](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019).

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database="db_book_reviews", table_name="raw_book_reviews", transformation_ctx="datasource0")

applymapping1 = ApplyMapping.apply(frame=datasource0, mappings=[
    ("Name", "string", "Name", "string"),
    ("Author", "string", "Author", "string"),
    ("User Rating", "double", "User Rating", "double"),
    ("Reviews", "int", "Reviews", "int"),
    ("Price", "int", "Price", "int"),
    ("Year", "int", "Year", "int"),
    ("Genre", "string", "Genre", "string")
], transformation_ctx="applymapping1")

resolvechoice2 = ResolveChoice.apply(frame=applymapping1, choice="make_struct", transformation_ctx="resolvechoice2")
dropnullfields3 = DropNullFields.apply(frame=resolvechoice2, transformation_ctx="dropnullfields3")

datasink1 = dropnullfields3.toDF().coalesce(1)
df_final_output = DynamicFrame.fromDF(datasink1, glueContext, "df_final_output")
datasink4 = glueContext.write_dynamic_frame.from_options(frame=df_final_output, connection_type="s3", connection_options={"path": "s3://book-reviews-cleansed-data/", "partitionKeys": ["Year", "Genre"]}, format="parquet", transformation_ctx="datasink4")

job.commit()

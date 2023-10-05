from pyspark.dbutils import DBUtils
from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()
dbutils = DBUtils(spark)


class {{cookiecutter.project_slug}}:
    # Get a game from dataframe based on name
    def example(string):
        """Example Method"""
        # column "_c0" is the name column in the video game dataset
        return str(string)

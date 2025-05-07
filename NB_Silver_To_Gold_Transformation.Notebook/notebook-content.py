# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "67e16447-42a3-4795-a46f-2deb7768b8b6",
# META       "default_lakehouse_name": "LH_Silver",
# META       "default_lakehouse_workspace_id": "938992c1-4258-4f54-9907-e07cb148742f",
# META       "known_lakehouses": [
# META         {
# META           "id": "67e16447-42a3-4795-a46f-2deb7768b8b6"
# META         },
# META         {
# META           "id": "78e1f90c-9375-4854-aef8-69752476891a"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.functions import round, current_date

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

silver_lakehouse_path = "abfss://HardwareSalesDev@onelake.dfs.fabric.microsoft.com/LH_Silver.Lakehouse/Tables/hardwaresales"
df = spark.read.format("delta").load(silver_lakehouse_path)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_enriched = df.withColumn("UnitPrice", round(df["Total"] / df["Quantity"], 2))
df_enriched = df_enriched.withColumn("lastupdate", current_date())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df_enriched)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

gold_lakehouse_path = ("abfss://HardwareSalesDev@onelake.dfs.fabric.microsoft.com/LH_Gold.Lakehouse/Tables/hardwaresales")
df_enriched.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(gold_lakehouse_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

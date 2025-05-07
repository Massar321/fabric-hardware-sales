# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "39cf925d-0c0a-440a-bb16-2140b77d5aa4",
# META       "default_lakehouse_name": "LH_Bronze",
# META       "default_lakehouse_workspace_id": "938992c1-4258-4f54-9907-e07cb148742f",
# META       "known_lakehouses": [
# META         {
# META           "id": "39cf925d-0c0a-440a-bb16-2140b77d5aa4"
# META         },
# META         {
# META           "id": "91fcfa86-eb9d-4071-8d08-0bc2e221a1a9"
# META         },
# META         {
# META           "id": "67e16447-42a3-4795-a46f-2deb7768b8b6"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

csv_path = "abfss://HardwareSalesDev@onelake.dfs.fabric.microsoft.com/LH_Bronze.Lakehouse/Files/dev_hardwaresales_data.csv"
df = spark.read.option("header", "true").option("inferSchema", "true").csv(csv_path)

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

delta_table_path = "abfss://HardwareSalesDev@onelake.dfs.fabric.microsoft.com/LH_Silver.Lakehouse/Tables/hardwaresales"
df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(delta_table_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

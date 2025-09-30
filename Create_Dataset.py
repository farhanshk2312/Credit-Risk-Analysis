from google.cloud import bigquery
from google.api_core.exceptions import Conflict

# Step 3a: Set your project and dataset
PROJECT = "project-portfolio-473015"   # replace with your project ID
DATASET = "credit_risk_main"       # desired dataset name

# Step 3b: Initialize BigQuery client
client = bigquery.Client(project=PROJECT)

# Step 3c: Create dataset
def create_dataset():
    dataset_ref = bigquery.Dataset(f"{PROJECT}.{DATASET}")
    dataset_ref.location = "US"  # choose location
    try:
        client.create_dataset(dataset_ref)
        print(f"Dataset {DATASET} created successfully!")
    except Conflict:
        print(f"Dataset {DATASET} already exists.")

# Step 3d: Create tables
def create_table():
    # --- Table 1: click_stream ---
    main_data_schema = [
        bigquery.SchemaField("id", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("member_id", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("loan_amnt", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("funded_amnt", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("funded_amnt_inv", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("term", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("int_rate", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("installment", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("grade", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("sub_grade", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("emp_title", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("emp_length", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("home_ownership", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("annual_inc", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("verification_status", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("issue_d", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("pymnt_plan", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("desc", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("purpose", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("title", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("zip_code", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("addr_state", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("dti", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("delinq_2yrs", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("earliest_cr_line", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("inq_last_6mths", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("mths_since_last_delinq", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("mths_since_last_record", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("open_acc", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("pub_rec", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("revol_bal", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("revol_util", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("total_acc", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("initial_list_status", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("out_prncp", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("out_prncp_inv", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("total_pymnt", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("total_pymnt_inv", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("total_rec_prncp", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("total_rec_int", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("total_rec_late_fee", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("recoveries", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("collection_recovery_fee", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("last_pymnt_d", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_pymnt_amnt", "FLOAT64", mode="REQUIRED"),
        bigquery.SchemaField("next_pymnt_d", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_credit_pull_d", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("collections_12_mths_ex_med", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("mths_since_last_major_derog", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("policy_code", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("application_type", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("annual_inc_joint", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("dti_joint", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("verification_status_joint", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("acc_now_delinq", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("tot_coll_amt", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("tot_cur_bal", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("open_acc_6m", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("open_il_6m", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("open_il_12m", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("open_il_24m", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("mths_since_rcnt_il", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("total_bal_il", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("il_util", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("open_rv_12m", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("open_rv_24m", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("max_bal_bc", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("all_util", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("total_rev_hi_lim", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("inq_fi", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("total_cu_tl", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("inq_last_12m", "FLOAT64", mode="NULLABLE"),
        bigquery.SchemaField("default_ind", "INT64", mode="REQUIRED"),
        bigquery.SchemaField("issue_date", "DATE", mode="NULLABLE"),
   
      
        ]
    table_id = f"{PROJECT}.{DATASET}.main_data"
    table = bigquery.Table(table_id, schema=main_data_schema)
    
    # Partition by ts and cluster by symbol
    table.time_partitioning = bigquery.TimePartitioning(
        type_=bigquery.TimePartitioningType.DAY,
        field="issue_date"
    )
    table.clustering_fields = ["member_id"]

    # Create table
    # for table in (click_stream_table):
    try:
            client.create_table(table)
            print(f"Table {table.table_id} created successfully!")
    except Conflict:
            print(f"Table {table.table_id} already exists.")

# Step 3e: Run creation
if __name__ == "__main__":
    create_dataset()
    create_table()

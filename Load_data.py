from google.cloud import bigquery

# Project / Dataset / Table names
PROJECT = "project-portfolio-473015"
DATASET = "credit_risk_main"
TABLE = "main_data"

client = bigquery.Client(project=PROJECT)

# Path to your flattened event metadata CSV file
csv_file_path = "data.csv"

# Reference to the table
table_id = f"{PROJECT}.{DATASET}.{TABLE}"

# Define schema for event_metadata table
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

# Job config
job_config = bigquery.LoadJobConfig(
    schema=main_data_schema,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,  # skip header row
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  # append to existing table
)

# Load CSV file into BigQuery
with open(csv_file_path, "rb") as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config
    )

# Wait for the load to finish
load_job.result()

# Confirm
destination_table = client.get_table(table_id)
print(f"Loaded {destination_table.num_rows} rows into {table_id}.")

import uuid
def convert_df_to_cosmos_db_format(df):
    
    cosmos_db_documents = []
    for _, row in df.iterrows():
        rate_document = {
            "id": str(uuid.uuid4()),
            "timestamp": f"{row['Date']}T{row['Time']}Z",
            "code": row['Currency_Type'],
            "telegraphic_transfers_buying_rate": float(row['Telegraphic_Transfers_Buying']) if row['Telegraphic_Transfers_Buying'] else None,
            "telegraphic_transfers_selling_rate": float(row['Telegraphic_Transfers_Selling']) if row['Telegraphic_Transfers_Selling'] else None,
            "currency_buying_rate": float(row['Currency_Buying']) if row['Currency_Buying'] else None,
            "currency_selling_rate": float(row['Currency_Selling']) if row['Currency_Selling'] else None,
            "bank": row['Bank'],
            "st_bank_code": row['ST BANK CODE']
        }
        cosmos_db_documents.append(rate_document)
    
    return cosmos_db_documents
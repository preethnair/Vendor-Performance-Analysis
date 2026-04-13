import pandas as pd
import os
import sqlite3
import logging
from Data_Injection import injest_db

logging.basicConfig(
    filename = 'Logs/get_vendor_summary.log',
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = 'a'
)

def Create_Vendor_Summary(con) :
    # Merge the final table : 
    VendorSalesSummery = pd.read_sql("""WITH FreighSummery AS (
    SELECT 
    VendorNumber, 
    SUM(Freight) AS FreightCost FROM vendor_invoice
    GROUP BY VendorNumber
    ),
    PurchaseSummery AS (
    SELECT 
    P.VendorNumber, 
    P.VendorName, 
    P.Brand, 
    P.Description, 
    P.PurchasePrice, 
    PP.Price AS ActualPrice, 
    PP.Volume, 
    SUM(P.Quantity) AS TotalPurchaseQuantity, 
    SUM(P.Dollars) AS TotalPurchaseDollars FROM purchases P JOIN purchase_prices PP 
    ON P.Brand = PP.Brand
    WHERE P.PurchasePrice > 0
    GROUP BY P.VendorNumber, P.VendorName, P.Brand, P.Description, P.PurchasePrice, PP.Price, PP.Volume
    ),
    SalesSummery AS (
    SELECT 
    VendorNo,
    Brand,
    SUM(SalesQuantity) TotalSalesQuantity, 
    SUM(SalesDollars) TotalSalesDollar,
    SUM(SalesPrice)TotalSalesPrice,
    SUM(ExciseTax) TotalExciseTax FROM sales
    GROUP BY VendorNo, Brand
    )
    SELECT
    PS.VendorNumber,
    PS.VendorName,
    PS.Brand,
    PS.Description,
    PS.PurchasePrice,
    PS.ActualPrice,
    PS.Volume,
    PS.TotalPurchaseQuantity,
    PS.TotalPurchaseDollars,
    SS.TotalSalesQuantity, 
    SS.TotalSalesDollar,
    SS.TotalSalesPrice,
    SS.TotalExciseTax,
    FS.FreightCost FROM PurchaseSummery PS LEFT JOIN SalesSummery SS
    ON PS.VendorNumber = SS.VendorNo AND PS.Brand = SS.Brand LEFT JOIN FreighSummery FS
    ON PS.VendorNumber = FS.VendorNumber
    ORDER BY PS.TotalPurchaseDollars DESC""", con)

    return VendorSalesSummery

def clean_data(df) :
    # Cleaning the Dataset :
    # 1.) Volume column has numeric data but datatype is object.
    df['Volume'] = df['Volume'].astype('float64')
    # 2.) TotalSalesQuantity, TotalSalesDollar, TotalSalesPrice,TotalExciseTax have 178 null values.
    VendorSalesSummery.fillna(0, inplace = True)
    # 3.) Some VendorName & Description have unnecessory space after their names. 
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # Creating new columns :
    df['GrossProfit'] = df['TotalSalesDollar'] - df['TotalPurchaseDollars']
    df['ProfutMargin'] = (df['GrossProfit'] / df['TotalSalesDollar']) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesPurchaseRatio'] = df['TotalSalesDollar'] / df['TotalPurchaseDollars']

    return df



if __name_ == '__main__' :
    #creating database connection
    con = sqlite3.connect('inventory.db')
    
    logging.info('Creating Vendor Summary Table')
    summary_df = Create_Vendor_Summary(con)
    logging.info(summary_df.head())

    logging.info('Cleaning Data')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())
    
    logging.info('Ingesting Data')
    injest_db(clean_df, 'VendorSalesSummery', con)
    logging.info('Complete')




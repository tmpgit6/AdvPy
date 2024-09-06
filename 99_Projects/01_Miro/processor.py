import pandas as pd
class Processor:

    def __init__(self,filename, output_file, del_col = None, num_col = None) -> None:
        self.filename = filename 
        self.df_backup = None
        self.df = None
        self.del_col = del_col
        self.num_col  = num_col
        self.output_file = output_file
        

    def read_csv(self):
        self.df_backup = pd.read_csv(self.filename)
        self.df = self.df_backup.copy()

    def delete_columns(self, cust_col_del = None):
        if self.del_col:
            self.df.drop(columns=self.del_col, inplace=True)
            self.del_col = None
        
        if self.cust_col_del:
            self.df.drop(columns=self.cust_col_del, inplace=True)

    def delete_nans(self):
        self.df = self.df.dropna(axis ="rows", how = "any" )

    def repeated_header(self):
        self.df = self.df.loc[ ~self.df["Order ID"].str.startswith("Ord")  ]

    def correct_datatypes(self):
        for col_name in self.num_col:
            self.df[col_name] = pd.to_numeric(self.df[col_name])
        
    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()

    def save_cleaned_file(self):
        self.df.to_csv(self.output_file, index = False)


    def clean(self):
        # Read CSV 
        self.read_csv() 

        # Delete unwanted columns
        self.delete_columns()

        # Delete NANs
        self.delete_nans()

        # Delete Repeated Header 
        self.repeated_header()  
        
        # Correct Data Types
        self.correct_datatypes()

        # Drop Duplicates
        self.drop_duplicates() 

        # Save the output File
        self.save_cleaned_file()
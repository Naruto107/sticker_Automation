import os
import pandas as pd
from fpdf import FPDF
from PIL import Image


folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'product entry')


csv_file = os.path.join(folder_path, 'products.csv')
data = pd.read_csv(csv_file)


template_path = os.path.join(folder_path, 'template.png')

class PDF(FPDF):
    def header(self):
        self.image(template_path, 0, 0, 210, 297)  

    def product_details(self, product_name, price, msrp, discount):
        self.set_xy(10, 50)  
        self.set_font("Times", style='B', size=16)  
        self.multi_cell(0, 10, f'Product: {product_name}')
        self.set_font("Times", size=14)  
        self.multi_cell(0, 10, f'MRP: {price}')
        self.multi_cell(0, 10, f'MSRP: {msrp}')
        self.multi_cell(0, 10, f'Discount: {discount}')


output_folder = os.path.join(folder_path, 'output')
os.makedirs(output_folder, exist_ok=True)

for index, row in data.iterrows():
    pdf = PDF()
    pdf.add_page()
    
    product_name = row['Product Name']
    price = row['Price']
    msrp = row['MSRP']
    discount = row['Discount']
    
    pdf.product_details(product_name, price, msrp, discount)
    
    output_file = os.path.join(output_folder, f'{product_name.replace(" ", "_")}.pdf')
    pdf.output(output_file)
    print(f'Created PDF: {output_file}')

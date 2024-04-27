#E-Commerce Ananlytics Dashboard

import matplotlib.pyplot as plt
import pandas as pd

def load_sales_data(file_path):
    return pd.read_excel(file_path)

def categorize_age_ranges(data):
    age_bins = [18, 26, 36, 46, 56] 
    age_labels = ['18-25', '26-35', '36-45', '46-55'] 
    data['Age Range'] = pd.cut(data['Customer Age'], bins=age_bins, labels=age_labels, right=False)
    return data

def plot_age_vs_referral(data):
    plt.subplot(2, 2, 1)
    age_referral_counts = data.groupby(['Age Range', 'Referral Source']).size().unstack(fill_value=0)
    age_referral_counts.plot(kind='bar', stacked=True, ax=plt.gca())
    plt.title('Customer Age vs Referral Source')
    plt.xlabel('Customer Age Range')
    plt.ylabel('Count')
    plt.legend(title='Referral Source')

def plot_discount_vs_category(data):
    plt.subplot(2, 2, 2)
    discount_category_counts = data.groupby(['Discount Information', 'Product Category']).size().unstack(fill_value=0)
    discount_category_counts.plot(kind='bar', stacked=True, ax=plt.gca())
    plt.title('Discount vs Product Category')
    plt.xlabel('Discount Information')
    plt.ylabel('Count')
    plt.legend(title='Product Category')

def plot_gender_vs_category(data):
    plt.subplot(2, 2, 3)
    gender_category_counts = data.groupby(['Customer Gender', 'Product Category']).size().unstack(fill_value=0)
    gender_category_counts.plot(kind='bar', stacked=True, ax=plt.gca())
    plt.title('Customer Gender vs Product Category')
    plt.xlabel('Customer Gender')
    plt.ylabel('Count')
    plt.legend(title='Product Category')

def plot_age_vs_payment(data):
    plt.subplot(2, 2, 4)
    age_referral_counts = data.groupby(['Age Range', 'Payment method']).size().unstack(fill_value=0)
    age_referral_counts.plot(kind='bar', stacked=True, ax=plt.gca())
    plt.title('Customer Age vs Payment method')
    plt.xlabel('Customer Age Range')
    plt.ylabel('Count')
    plt.legend(title='Payment method')

def main():
    file_path = "D:\Python programs\e_commerce_data.xlsx"
    sales_data = load_sales_data(file_path)
    sales_data = categorize_age_ranges(sales_data)

    plt.figure(figsize=(10, 6))

    plot_age_vs_referral(sales_data)
    plot_discount_vs_category(sales_data)
    plot_gender_vs_category(sales_data)
    plot_age_vs_payment(sales_data)

    plt.tight_layout()
    plt.show()

main()
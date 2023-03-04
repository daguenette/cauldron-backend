from input_functions import form_step1
import taxes_allocations as tax_alloc

user_data = form_step1()


## --- Summary ---

a = user_data[0]['salary_income']
b = user_data[0]['salary_income']
c = user_data[0]['salary_income']
d = user_data[0]['salary_income']

data = {

    'Annual_income': tax_alloc.calculate_annual_income_tax(a, b),
    'Federal_income': tax_alloc.calculate_federal_tax(a, b)

}





print(f"If you make {data['Feral_Income']} a year living in Québec, you will be taxed {b}. That means your net pay will be {c} per year, or {d} per month.")
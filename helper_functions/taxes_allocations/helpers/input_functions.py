## Inputs


def form_step1():

    form_response = {

        "user": 1,
        "year": input("Planification year: "),
        "salary_income": input("What is your salaried annual income: "),
        "salary_hours": input("How many hours are you working per week: "),
        "salary_frequency": input("How frequently are you getting paid: "),
        "freelance_income": input("What is your freelance annual income: "),
        "freelance_hours": input("How many freelance hours are you working per week: "),
        "capital_gains": input("What is the amount of capital gains you made this year: "),
        "eligible_dividends": input("What is the amount of eligible dividends you made this year: "),
        "non_eligible_dividends": input("What is the amount of eligible dividends you made this year: "),
        "other_incomes": input("What is the amount of other eligible income(s) you made this year: "),
        "tax_paid_on_incomes": input("If relevant, what is the amount of taxes you alreay paid on incomes this year: "),
        "rrsp_personal": input("What is the contribution amount you made/intend to make to your personal RRSP this year: "),
        "rrsp_joined": input("If relevant, what is the contribution amount you made/intend to make to your joined RRSP this year: "),
        "other_deductions": input("Do you have an amount for other deductions you can claim this year (medical, donations, etc.): "),
        "nbr_of_children": input("If relevant, how many children do you have: "),
        "user_age":input("How old are you: "),
        "canada_entry_date":input("If relevant, what is the date of your entry in Canada: "),
        "rrsp_contributions_total":input("The total amount contributed to your RRSP(s) over the years: "),
        "tfsa_contributions_total":input("The total amount contributed to your TFSA(s) over the years: "),
        "tfsa_contribution_year":input("The total amount contributed to your TFSA(s) for this year: "),
        "mortage_open":input("Do you have a mortgage: "),
        "mortgage_principal":input("Principal amount of your mortgage: "),
        "mortgage_current_principal":input("Current principal amount of your mortgage left to be reimbursed: "),
        "mortgage_rate":input("What is your mortgage rate: "),
        "mortgage_total_duration_years":input("What is your mortgage total duration (years): "),
        "mortgage_rate_duration":input("If your rate is fixed, how many months are left before reevaluation: "),
        "high_debt_open":input("Do you have any high interest debts: "),
        "debt_amount":input("What is the current amount you owe: "),
        "debt_rate":input("What is the rate on that debt: "),
        "monthly_total_income":input("What is your monthly net income: "),
        "monthly_mandatory_expenses":input("What is the total amount of your monthly mandatory expenses: "),
        "monthly_food_expenses":input("What is the average total amount of your monthly food expenses: "),
        "monthly_car_expenses":input("What is the average total amount of your monthly mandatory expenses: "),
        "monthly_optional_expenses":input("What is the average total amount of your optional expenses: "),
        "risk_level":input("What risk level are you confortable with regarding your safety net (in months): "),
        "safety_net_current_amount":input("What is the current amount of readily available cash you have in your safety net: "),
        "year_current_rrsp_contribution":input("What is the current amount you contributed to your RRSP for this year: "),
        "year_current_resp_contribution":input("What is the current amount you contributed to this RESP for this year: "), ### Create a loop for RESP
        "total_current_tfsa_contribution":input("What is the current amount you contributed to this TFSA for this year: ")
    
    }

    ## Inialize children age array - ADD HERE LOOP FOR RESP YES NO IF YES THEN CONTRIBUTION YEAR 1, 2, X, X being the age of the child
    children_ages = []

    for child in range(int(form_response["nbr_of_children"])):
        children_ages.append(int(input(f"Age of child {child + 1}: ")))

    form_response["age_of_children"] = children_ages

    return form_response
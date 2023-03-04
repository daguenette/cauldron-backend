## Inputs


def form_step1():

    ## Planification year first so it become the id:
    planification_year = input("Planification year: ")

    form_response = {

        planification_year: {
            
            "salary_income": input("Income: "),
            "salary_hours": input("Hours: "),
            "salary_frequency": input("Frequency: "),
            "freelance_income": input("Freelance income: "),
            "freelance_hours": input("Freelance hours: "),
            "capital_gains": input("Capital gains: "),
            "eligible_dividends": input("Eligible Dividends: "),
            "non_eligible_dividends": input("Non Eligible Dividends: "),
            "other_incomes": input("Other incomes: "),
            "tax_paid_on_incomes": input("Tax paid on incomes: "),
            "rrsp_personal": input("Personal RRSP: "),
            "rrsp_joined": input("Joined RRSP: "),
            "other_deductions": input("Other deductions: "),
            "nbr_of_children": input("Number of children: ")
            
        } 

    }

    ## Inialize children age array
    children_ages = []

    for child in range(int(form_response[planification_year]["nbr_of_children"])):
        children_ages.append(int(input(f"Age of child {child + 1}: ")))

    form_response[planification_year]["age_of_children"] = children_ages

    return form_response
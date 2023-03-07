from input_functions import form_step1
import taxes_allocations as tax_alloc

user_data = form_step1()


## --- Input data Summary ---

a = user_data[0]['salary_income']
b = user_data[1]['salary_hours']
c = user_data[2]['salary_frequency']
d = user_data[3]['freelance_income']
e = user_data[4]['freelance_hours']
f = user_data[5]['capital_gains']
g = user_data[6]['eligible_dividends']
h = user_data[7]['non_eligible_dividends']
i = user_data[8]['other_incomes']
j = user_data[9]['tax_paid_on_incomes']
k = user_data[10]['rrsp_personal']
l = user_data[11]['rrsp_joined']
m = user_data[12]['other_deductions']
n = user_data[13]['nbr_of_children']
o = user_data[14]['user_age']
p = user_data[15]['canada_entry_date']
q = user_data[16]['rrsp_contributions_total']
r = user_data[17]['tfsa_contributions_total']
s = user_data[18]['tfsa_contribution_year']
t = user_data[19]['mortage_open']
u = user_data[20]['mortgage_principal']
v = user_data[21]['mortgage_current_principal']
x = user_data[22]['mortgage_rate']
y = user_data[23]['mortgage_total_duration_years']
z = user_data[24]['mortgage_rate_duration']
a1 = user_data[25]['high_debt_open']
b1 = user_data[26]['debt_amount']
c1 = user_data[27]['debt_rate']
d1 = user_data[28]['monthly_total_income']
e1 = user_data[29]['monthly_mandatory_expenses']
f1 = user_data[30]['monthly_food_expenses']
g1 = user_data[31]['monthly_car_expenses']
h1 = user_data[32]['monthly_optional_expenses']
i1 = user_data[33]['risk_level']
j1 = user_data[34]['safety_net_current_amount']
k1 = user_data[35]['year_current_rrsp_contribution']
l1 = user_data[36]['year_current_resp_contribution']
m1 = user_data[37]['total_current_tfsa_contribution']

## --- Summary of the financial situation based on input data = {

  ## ---  'Annual_income': tax_alloc.calculate_annual_income_tax(a, b),
  ## ---  'Federal_income': tax_alloc.calculate_federal_tax(a, b)

## --- }


print(form_step1)

print(f" TAXES ET ALLOCATIONS - Recap chiffres")
print(f"Montant total des revenus imposables")
print(f"Montant total des taxes (XX%)")
print(f"Sub - Montant total des taxes fédérales")
print(f"Sub - Montant total des taxes provinciales")
print(f"Sub - Montant total des QPP/QPIP/El premiums")
print(f"Sub - Afficher le taux dimposition moyen")
print(f"Sub - Afficher le taux dimposition marginal")
print(f"Revenu net après taxes")
print(f"Sub - Pourcentage du revenu brut (XX%)")
print(f"Montant total des allocations familliales")
print(f"Sub - Montant des allocations familliales FED")
print(f"Sub - Montant des allocations familliales QC")

print(f"TAXES ET ALLOCATIONS - Sommaire expliqué")
print(f"If you make $12,323,123 a year living in Québec, you will be taxed $6,542,585. That means your net pay will be $5,780,538 per year, or $481,712 per month.")
print(f"Your average tax rate is 53.09% and your marginal tax rate is 53.31%.")
print(f"This marginal tax rate means your immediate additional income will be taxed at this rate.")
print(f"For instance, an increase of $100 in your salary will be taxed $53, meaning that your net pay will increase by $47.")
print(f"As your hourly rate is $XX, it means that any additional hour worked will increase your revenue by $XX, or the last XX minutes of the hour.")
print(f"Votre revenu imposable permet daccéder à un montant annuel dallocations familales $XX (Fed XX + QC XX), soit XX par mois.")

print(f"GESTION DES PANIERS - ANNEE XXXX")
print(f"Revenu mensuel net dimpôts moyen de lannée précédente :")
print(f"Dépenses mensuelles en moyenne :")
print(f"READY TO INVEST - Revenu mensuel net dimpôts qui peut être placé dans les paniers :")
print(f"Total à placer pour lannee :")
print(f"TOTAL RESTANT A PLACER POUR Lannee :")
print(f"MOIS RESTANTS POUR REMPLIR LE TOTAL A PLACER :")
print(f"PROGRESSION :")

print(f"FILET DE SECURITE")
print(f"Le filet de sécurité est une assurance daccès à de largent disponible immédiatement en cas de pépin de la vie. Il est recommandé dy placer un minimum de 6 mois de dépenses mensuelles moyennes.")
print(f"Definir votre niveau de risque : XX mois")
print(f"Dépenses mensuelles en moyenne :")
print(f"Inflation de lannée précédente :")
print(f"Montant total du filet :")
print(f"Montant en cours :")
print(f"Montant restant à accumuler :")
print(f"Mois restants :")
print(f"Progression : XX%")

print(f"REER ou RRSP")
print(f"Maximum contribution REER:")
print(f"Contribution REER prévue cette année : (prérempli avec montant si demandes envoyées)")
print(f"Contribution REER actuelle :")
print(f"Mois restants :")
print(f"Montant requis par mois pour remplir le REER au maximum de la contribution possible avant le 1er Mars :")
print(f"Progression : XX%")

print(f"RESP")
print(f"Contribution actuelle :")
print(f"Limite maximale de contribution : $50,000")
print(f"Bourse maximum par an : $500")
print(f"Contribution pour atteindre la bourse maximum (20%) : $2500")
print(f"Contribution RESP année en cours :")
print(f"Contribution restante pour atteindre la bourse maximum :")
print(f"Mois restants :")
print(f"Montant requis par mois pour remplir le RESP au maximum de la contribution possible avant le 31 décembre :")
print(f"Progression : XX%")

print(f"TFSA")
print(f"Contribution totale : (calculée auto avec âge)")
print(f"Contribution ajoutée cette année : $6000")
print(f"Contribution totale actuelle :")
print(f"Contribution totale restante :")
print(f"Progression :  XX% ")
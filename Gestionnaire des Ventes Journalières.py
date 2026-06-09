# إعداد البيانات في البداية
number_des_jours = int(input("How much you want to subscribe: "))


# لاضافة ايام البيع للقائمة
def ajouter_journees(les_jours , num_jours):
    for i in range(0 , num_jours):
        les_jours.append(f"Jour {i+1}")
# لاضافة الكمية المباعة او مبلغ المباع
def ajouter_element(les_jours , montants):
    for i in range(len(les_jours)):
        montant = float(input(f"How much did you sell in {les_jours[i]}: "))
        montants.append(montant)
# دالة لفرز الايام و المبالغ في قاموس
def remplir_dictionnaire(jours , montant , dico):
    for i in range(len(jours)):
        dico[jours[i]] = montant[i]
# دالة لحساب المجموع المباع
def calculer_total(montent):
    total = 0
    for m in montent:
        total += m
    return total
# دالة لمعرفة اكثر يوم تم البيع فيه
def meilleur_ventes(les_jours):
    max_ventes = 0
    jour_max = ""
    for jour, montant in les_jours.items():
        if montant > max_ventes:
            max_ventes = montant
            jour_max = jour
    return jour_max, max_ventes

# البرنامج الرئيسي
# هنا نقوم بتهيئة القوائم و القاموس
days_list = []
ajouter_journees(days_list , number_des_jours)
sales_amounts = []
ajouter_element(days_list , sales_amounts)
les_journees = {}
remplir_dictionnaire(days_list , sales_amounts , les_journees)



# هنا نقوم بعرض القائمة للمستخدم
while True:
    print("\nMenu :")
    print("1. Afficher un journee")
    print("2. Ajouter une nouvelle journée")
    print("3. Calculer le total des ventes")
    print("4. Afficher le meilleur jour de ventes")
    print("5. Quitter")

    choix = int(input("\nEntrez votre choix: "))

    if choix == 1:
        print("\nListe des journées et montants:")
        for jours in les_journees.keys():
            print(f"{jours} => {les_journees[jours]} DA")

    elif choix == 2:
        new_day = f"Jour {len(days_list)+1}"
        amount = float(input(f"How much did you sell in {new_day}: "))
        days_list.append(new_day)
        sales_amounts.append(amount)
        les_journees[new_day] = amount

    elif choix == 3:
        total_montant = calculer_total(sales_amounts)
        print(f"\nLe total des ventes est {total_montant} DA.")

    elif choix == 4:
        jour , montant = meilleur_ventes(les_journees)
        if jour:
            print(f"\nLe meilleur jour de ventes est {jour} avec {montant} DA.")
        else:
            print("\nNo sales data available.")

    elif choix == 5:
        print("\nAu revoir!\n")
        break

    else:
        print("\nChoix invalide. Veuillez réessayer.\n")


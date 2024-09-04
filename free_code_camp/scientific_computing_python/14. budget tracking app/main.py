class Category:
    """
    author: Teun Jansen
    Deze klasse representeert een budgetcategorie (bijv. voedsel, kleding).
    """
    def __init__(self, name):
        """
        Initialiseert een nieuwe categorie met de opgegeven naam.
        """
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Voegt een storting toe aan de categorie.
        Args:
            amount: Het bedrag dat wordt gestort.
            description: Een optionele beschrijving van de storting.
        """
        self.ledger.append({"amount": amount, "description": description[:23]})

    def withdraw(self, amount, description=""):
        """
        Probeert een bedrag op te nemen van de categorie.
        Args:
            amount: Het bedrag dat wordt opgenomen.
            description: Een optionele beschrijving van de opname.
        Returns:
            True als de opname is geslaagd, anders False.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description[:23]})
            return True
        return False

    def get_balance(self):
        """
        Berekent het huidige saldo van de categorie.
        Returns:
            Het saldo van de categorie.
        """
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        """
        Verplaatst een bedrag van deze categorie naar een andere.
        Args:
            amount: Het bedrag dat wordt overgemaakt.
            other_category: De categorie waarnaar het bedrag wordt overgemaakt.
        Returns:
            True als de overboeking is geslaagd, anders False.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """
        Controleert of er voldoende saldo is voor een transactie.
        Args:
            amount: Het bedrag dat wordt gecontroleerd.
        Returns:
            True als er voldoende saldo is, anders False.
        """
        return self.get_balance() >= amount

    def __str__(self):
        """
        Geeft een leesbare representatie van de categorie.
        Returns:
            Een string met de naam van de categorie, de transacties en het totaal.
        """
        title = f"*{self.name.center(30, '*')}"
        ledger_items = "\n".join(f"{item['description'].ljust(23)}{item['amount']:>7.2f}" for item in self.ledger)
        total = f"\nTotal: {self.get_balance():>7.2f}"
        return title + "\n" + ledger_items + total

def create_spend_chart(categories):
    """
    Creëert een grafiek die het totale bedrag weergeeft dat in elke categorie is uitgegeven.
    Args:
        categories: Een lijst van Category-objecten.
    Returns:
        Een string die de grafiek representeert.
    """
    categories_data = {}
    for category in categories:
        total_spent = sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        categories_data[category.name] = total_spent

    max_spent = max(categories_data.values())
    num_bars = 10
    bar_length = int(max_spent / num_bars)

    chart = f"{'  '}|{' ' * (num_bars * 2 + 1)}\n"
    for i in range(num_bars, 0, -1):
        chart += f"{i:2d}|"
        for category, total_spent in categories_data.items():
            if total_spent >= i * bar_length:
                chart += "  o  "
            else:
                chart += "     "
        chart += "\n"
    chart += f"{'  '}|{' ' * (num_bars * 2 + 1)}\n{'  '}|-"
    chart += f"{'-' * (num_bars * 2 + 1)}\n{'  '}|{' ' * (num_bars * 2 + 1)}\n{'  '}|"
    for category in categories:
        chart += f" {category.name[:3].rjust(3)}"
    return chart
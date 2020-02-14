class Product():
    """ Creates Product class for Acme Corporation."""

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """Defines attributes for the product using constructor."""
        from random import randint
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

     def stealability(self):
        """Estimates the likelihood of theft as a method using the weight and price."""
        theft = self.price / self.weight
        if steal < 0.5:
            return "Low Theft Risk."
        elif steal < 1:
            return "Moderate Theft Risk."
        else:
            return "High Theft Risk."

      def explode(self):
        """Estimates the likelihood of explosion as a method using the flammability and weight."""
        explosion = self.flammability * self.weight
        if explosion < 10:
            return "Low Explosive Risk"
        elif explosion < 50:
            return "Moderate Explosive Risk"
        else:
            return "High Explosive Risk"

        class BoxingGlove(Product):
    """Creating the Child class BoxingGlove from the Product class above."""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    """Override explode method created in the parent class Product."""

    def explode(self):
        return "Boxing Glove"

    """Evaluates the product weight to evaluate shipping costs."""
    def weight(self):
        if self.weight < 5:
            return "Low Weight."
        elif self.weight < 15:
            return "Moderate Weight."
        else:
            return "Heavy Weight."

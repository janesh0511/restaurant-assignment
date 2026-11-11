class MenuItem:
    def __init__(self, dish_name, price, is_vegetarian):
        self._dish_name = dish_name
        self._price = price
        self._is_vegetarian = is_vegetarian

    def get_description(self):
        veg_status = "Vegetarian" if self._is_vegetarian else "Non-Vegetarian"
        return f"{self._dish_name} - ${self._price:.2f} ({veg_status})"

    def display_item(self):
        print(self.get_description())


class Appetizer(MenuItem):
    def __init__(self, dish_name, price, is_vegetarian, sharing_size):
        super().__init__(dish_name, price, is_vegetarian)
        self._sharing_size = sharing_size

    def get_description(self):
        return f"[Appetizer] {self._dish_name} - ${self._price:.2f} | Size: {self._sharing_size}"

    def apply_happy_hour_discount(self):
        self._price = self._price * 0.80
        print(f"Happy hour discount applied! New price: ${self._price:.2f}")


class Dessert(MenuItem):
    def __init__(self, dish_name, price, is_vegetarian, sugar_level_grams):
        super().__init__(dish_name, price, is_vegetarian)
        self.__sugar_level_grams = sugar_level_grams

    def get_description(self):
        return f"[Dessert] {self._dish_name} - ${self._price:.2f} | Sugar: {self.__sugar_level_grams}g"

    def add_extra_scoop(self):
        self.__sugar_level_grams += 15
        print(f"Extra scoop added! Sugar level is now {self.__sugar_level_grams}g")


if __name__ == "__main__":
    print("--- VERIFICATION TEST OUTPUT ---")
    
    base_item = MenuItem("Generic Food", 5.99, True)
    base_item.display_item()

    app = Appetizer("Spinach Dip", 9.99, True, "Large")
    app.display_item()
    app.apply_happy_hour_discount()
    app.display_item()

    dessert = Dessert("Chocolate Cake", 7.50, True, 45)
    dessert.display_item()
    dessert.add_extra_scoop()
    dessert.display_item()
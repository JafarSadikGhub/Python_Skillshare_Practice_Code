class Ereader():

    def __init__(self, make, model, backlight, battery, screen_type):

        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        """ attribute default value """
        self.library_count = 0
    
    def get_ereader_name(self):

        long_name = self.make + " - " + self.model + " - " + self.backlight + " - " + self.battery + " - " + self.screen_type
        return long_name.title()
    
    def read_library_count(self):
        print("You have " + str(self.library_count) + " books in your kindle library.")
    
    def update_library_count(self, ebook_count):
        self.library_count = ebook_count
    
    def increment_library_count(self, purchased_ebooks):
        self.library_count += purchased_ebooks


class Screen():

    def __init__(self, screen_resolution = '1280* 800'):
        self.screen_resolution = screen_resolution
    def describe_screen(self):
        print("\nFire HD 8 features a widescreen " + self.screen_resolution + " HD screen.")


my_new_erader = Ereader('Amazon Kindle', 'paperwhite', 'adjustable', 'several months of battery life', '361dpi')
print(my_new_erader.get_ereader_name())
### my_new_erader.read_library_count()
"""Modifying value directly"""
###my_new_erader.library_count = 36
"""my_new_erader.update_library_count(48)
my_new_erader.read_library_count()
my_new_erader.increment_library_count(5)
my_new_erader.read_library_count()"""

"""Creating a child class..."""
class KindleFire(Ereader):

    def __init__(self, make, model, backlight, battery, screen_type):
        
        super().__init__(make, model, backlight, battery, screen_type)
        self.firescreen = Screen()

    



my_kindle_fire = KindleFire('amazon', 'kindle fire', 'backlight', '12 hrs battery life', 'color screen')
print(my_kindle_fire.get_ereader_name())

"""my_kindle_fire.describe_screen()""" 
my_kindle_fire.firescreen.describe_screen()
"""my_k = Screen()
my_k.describe_screen()"""
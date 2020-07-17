#from fn_ereader_class_for_importing_multiple_module import Ereader, KindleFire
import fn_ereader_class_for_importing_multiple_module

my_new_ereader = fn_ereader_class_for_importing_multiple_module.Ereader('amazon', 'paperweight', 'adjustable backlight', 'several months of battery life', '360dpi')
print(my_new_ereader.get_ereader_name())

my_color_ereader = fn_ereader_class_for_importing_multiple_module.KindleFire('amazon', 'kindle fire', 'color screen', '12 hours of battery life', '1280 * 720')
print(my_color_ereader.get_ereader_name())
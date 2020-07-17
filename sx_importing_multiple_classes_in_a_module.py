from fn_ereader_class_for_importing_multiple_module import KindleFire

my_kindle_fire = KindleFire('amazon', 'kindle fire', 'color screen', '12 hour battery life', '12080 * 720')
print(my_kindle_fire.get_ereader_name())
print(my_kindle_fire.firescreen.describe_screen())
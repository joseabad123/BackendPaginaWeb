
# Django imports
from django.contrib import admin

# Local imports
from core.models import (User,
                          Category,
                          Content,
                          Content_Media,
                          Event,
                          Group,
                          Group_Contact,
                          Group_Event,
                          Item_Category,
                          Menu_Item,
                          Person,
                          Person_Contact,
                          Person_Media,
                          Person_Role,
                          Person_Section,
                          Role,
                          Section,
                          Subject_Matter,
                          Requirement)
from core.custom_admin import (Item_Category_Admin,
                            Section_Admin,
                            Subject_Matter_Admin)

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Content)
admin.site.register(Content_Media)
admin.site.register(Event)
admin.site.register(Group)
admin.site.register(Group_Contact)
admin.site.register(Group_Event)
admin.site.register(Item_Category, Item_Category_Admin)
admin.site.register(Menu_Item)
admin.site.register(Person)
admin.site.register(Person_Contact)
admin.site.register(Person_Media)
admin.site.register(Person_Role)
admin.site.register(Person_Section)
admin.site.register(Role)
admin.site.register(Section, Section_Admin)
admin.site.register(Subject_Matter, Subject_Matter_Admin)
admin.site.register(Requirement)



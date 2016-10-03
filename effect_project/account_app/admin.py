from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from account_app.forms import GeneralUserCreationForm, GeneralUserChangeForm
from account_app.models import EmailBasedUser, TypeGUser, TypeCUser, Skills, Position, ExpertiseArea


class GeneralUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = GeneralUserChangeForm
    add_form = GeneralUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin', 'user_type')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(EmailBasedUser, GeneralUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

admin.site.register(TypeGUser)
admin.site.register(TypeCUser)
admin.site.register(Skills)
admin.site.register(Position)
admin.site.register(ExpertiseArea)
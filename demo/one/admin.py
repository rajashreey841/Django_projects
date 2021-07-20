from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from one.models import One


class OneAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(One, OneAdmin)


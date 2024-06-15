from django.contrib import admin
from home_module.models import Expense, Income

#
# class ExpenseModelAdmin(admin.ModelAdmin):
#     fields = '__all__'
#     list_editable = ['amount']


admin.site.register(Expense)
admin.site.register(Income)


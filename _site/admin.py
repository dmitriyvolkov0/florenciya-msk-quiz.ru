from django.contrib import admin
from .models import SiteSettings, FirstScreenSettings, Gift

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description')
        }),
        ('Контакты', {
            'fields': ('phone', 'phone_moderate', 'city', 'street')
        }),
        ('Рабочее время', {
            'fields': ('work_time',)
        }),
        ('Модерация', {
            'fields': ('is_moderate',)
        }),
    )

    def has_add_permission(self, request):
        # Запрещаем добавление новых записей, если уже есть одна
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление записи
        return False
    

@admin.register(FirstScreenSettings)
class FirstScreenSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'subtitle', 'location')
        }),
        ('Врач', {
            'fields': ('employee_experience', 'employee_profession', 'employee_fio')
        }),
        ('Услуга 1', {
            'fields': ('service_1_title', 'service_1_old_price', 'service_1_new_price')
        }),
        ('Услуга 2', {
            'fields': ('service_2_title', 'service_2_old_price', 'service_2_new_price')
        }),
        ('Подарки', {
            'fields': ('gifts_title', 'gifts',)
        }),
    )

    def has_add_permission(self, request):
        return not FirstScreenSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(Gift)
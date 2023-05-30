from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_otp.decorators import otp_required
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from parler.admin import TranslatableAdmin

from governanceplatform.models import Company, Sector, User, Services
from governanceplatform.settings import SITE_NAME


# Customize the admin site
class CustomAdminSite(admin.AdminSite):
    site_header = SITE_NAME + " " + _("Administration")
    site_title = SITE_NAME

    def admin_view(self, view, cacheable=False):
        decorated_view = otp_required(view)
        return super().admin_view(decorated_view, cacheable)


admin_site = CustomAdminSite()


class SectorResource(resources.ModelResource):
    id = fields.Field(
        column_name="id",
        attribute="id",
    )

    name = fields.Field(
        column_name="name",
        attribute="name",
    )

    parent = fields.Field(
        column_name="parent",
        attribute="parent",
        widget=ForeignKeyWidget(Sector, field="name"),
    )

    class Meta:
        model = Sector


@admin.register(Sector, site=admin_site)
class SectorAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ["name", "parent"]
    search_fields = ["name"]
    resource_classes = [SectorResource]

class ServicesResouce(resources.ModelResource):
    id = fields.Field(
        column_name="id",
        attribute="id",
    )

    name = fields.Field(
        column_name="name",
        attribute="name",
    )

    sector = fields.Field(
        column_name="sector",
        attribute="sector",
        widget=ForeignKeyWidget(Sector, field="name"),
    )

    class Meta:
        model = Sector

@admin.register(Services, site=admin_site)
class ServicesAdmin(ImportExportModelAdmin, TranslatableAdmin):
    list_display = ["name", "sector"]
    search_fields = ["name"]
    resource_classes = [ServicesResouce]


class CompanyResource(resources.ModelResource):
    id = fields.Field(column_name="id", attribute="id")
    identifier = fields.Field(column_name="identifier", attribute="identifier")
    name = fields.Field(column_name="name", attribute="name")
    address = fields.Field(column_name="address", attribute="address")
    country = fields.Field(column_name="country", attribute="country")
    email = fields.Field(column_name="email", attribute="email")
    phone_number = fields.Field(column_name="phone_number", attribute="phone_number")
    is_regulator = fields.Field(column_name="is_regulator", attribute="is_regulator")
    monarc_path = fields.Field(column_name="monarc_path", attribute="monarc_path")
    sectors = fields.Field(
        column_name="sectors",
        attribute="sectors",
        widget=ManyToManyWidget(Sector, field="name", separator=","),
    )

    class Meta:
        model = Company


@admin.register(Company, site=admin_site)
class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [CompanyResource]
    list_display = [
        "name",
        "address",
        "country",
        "email",
        "phone_number",
        "get_sectors",
        "is_regulator",
    ]
    list_filter = ["is_regulator", "sectors"]
    search_fields = ["name"]
    filter_horizontal = ("sectors", "sectors")

    fieldsets = [
        (
            _("Contact Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    "name",
                    ("address", "country"),
                    ("email", "phone_number"),
                ],
            },
        ),
        (
            _("Configuration Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    ("is_operateur",),
                    "identifier",
                    "monarc_path",
                    "sectors",
                ],
            },
        ),
    ]


class UserResource(resources.ModelResource):
    id = fields.Field(column_name="id", attribute="id")
    first_name = fields.Field(column_name="first_name", attribute="first_name")
    last_name = fields.Field(column_name="last_name", attribute="last_name")
    email = fields.Field(column_name="email", attribute="email")
    phone_number = fields.Field(column_name="phone_number", attribute="phone_number")
    is_administrator = fields.Field(
        column_name="is_administrator", attribute="is_administrator"
    )
    companies = fields.Field(
        column_name="companies",
        attribute="companies",
        widget=ManyToManyWidget(Sector, field="name", separator=","),
    )
    sectors = fields.Field(
        column_name="sectors",
        attribute="sectors",
        widget=ManyToManyWidget(Sector, field="name", separator=","),
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "is_administrator",
            "companies",
            "sectors",
        ]


class sectorInline(admin.TabularInline):
    model = User.sectors.through

@admin.register(User, site=admin_site)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [UserResource]
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "get_companies",
        "get_sectors",
        "is_administrator",
    ]
    search_fields = ["first_name", "last_name", "email"]
    list_filter = [
        "sectors",
        "is_administrator",
    ]

    filter_horizontal = ("companies", "sectors")

    list_display_links = ("email", "first_name", "last_name")

    fieldsets = [
        (
            _("Contact Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    ("first_name", "last_name"),
                    ("email", "phone_number"),
                    "companies",
                ],
            },
        ),
        (
            _("Configuration Information"),
            {
                "classes": ["extrapretty"],
                "fields": [
                    "is_administrator",
                ],
            },
        ),
    ]

    inlines = (sectorInline,)
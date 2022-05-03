# Generated by Django 2.2.6 on 2019-11-14 07:28

from django.db import migrations


class Renamer:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new

    def __call__(self, apps, schema_editor):
        Autorisatie = apps.get_model("authorizations.Autorisatie")
        for autorisatie in Autorisatie.objects.all():
            scopes = [self.patch_scope(scope) for scope in autorisatie.scopes]
            if scopes == autorisatie.scopes:
                continue

            autorisatie.scopes = scopes
            autorisatie.save(update_fields=["scopes"])

    def patch_scope(self, scope: str) -> str:
        if not scope.startswith(f"{self.old}."):
            return scope
        return scope.replace(f"{self.old}.", f"{self.new}.", 1)


class Migration(migrations.Migration):

    dependencies = [
        ("authorizations", "0010_auto_20190712_1643"),
    ]

    operations = [
        migrations.RunPython(
            Renamer("zaaktypes", "catalogi"),
            Renamer("catalogi", "zaaktypes"),
        )
    ]

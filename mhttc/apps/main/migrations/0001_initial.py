# Generated by Django 3.0.8 on 2020-10-30 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormTemplate",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "time_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Template Updated or completed at.",
                        verbose_name="date modified",
                    ),
                ),
                ("start_date", models.DateTimeField(verbose_name="project start date")),
                ("end_date", models.DateTimeField(verbose_name="project end date")),
                (
                    "name",
                    models.TextField(
                        help_text="Evidence-Based Intervention/Program/Service Being Implemented (WHAT)"
                    ),
                ),
                (
                    "target_audience_who",
                    models.TextField(
                        help_text="Who is the audience (including type of organizations)"
                    ),
                ),
                (
                    "target_audience_disciplines",
                    models.TextField(help_text="Specify discipline(s)"),
                ),
                (
                    "target_audience_roles",
                    models.TextField(help_text="Specify role(s)"),
                ),
                (
                    "target_audience_across_orgs",
                    models.BooleanField(
                        default=False,
                        help_text="Multiple individuals across organizations",
                    ),
                ),
                (
                    "target_audience_within_org",
                    models.BooleanField(
                        default=False,
                        help_text="Multiple individuals within an organization",
                    ),
                ),
                (
                    "target_audience_teams_across_orgs",
                    models.BooleanField(
                        default=False,
                        help_text="Multiple individuals or teams across organizations",
                    ),
                ),
                (
                    "implement_strategy_description",
                    models.TextField(
                        help_text="Free Text Description (Provide a Description of the Planned Implementation Steps)"
                    ),
                ),
                (
                    "consider_system_factors",
                    models.TextField(
                        help_text="System factors--external to the organization (e.g., financing; mandates, community, culture)"
                    ),
                ),
                (
                    "consider_org_factors",
                    models.TextField(
                        help_text="Organizational factors—internal to the organization (e.g., leadership; readiness)"
                    ),
                ),
                (
                    "consider_clinical_factors",
                    models.TextField(
                        help_text="Individual clinician factors (e.g., alignment with existing practice; complexity)"
                    ),
                ),
                (
                    "consider_sustainment_strategy",
                    models.TextField(
                        blank=True,
                        help_text="Sustainment strategies applied",
                        null=True,
                    ),
                ),
                (
                    "implementation_recruited",
                    models.TextField(help_text="How will participants be recruited?"),
                ),
                (
                    "implementation_participants",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="How many participants are enrolled?",
                        null=True,
                    ),
                ),
                (
                    "implementation_enrolled",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="# (%) initiating implementation strategy (individuals, teams or organizations)",
                        null=True,
                    ),
                ),
                (
                    "outcome_reach",
                    models.TextField(
                        help_text="Reach (# or percentage of population, what is the population, and how will you be measuring the outcome?"
                    ),
                ),
                (
                    "outcome_effectiveness",
                    models.TextField(
                        help_text="Effectiveness of Intervention/Program/Services (w/consumers), how will you measure it?"
                    ),
                ),
                (
                    "outcome_adoption",
                    models.TextField(
                        help_text="Number of providers? How will you be measuring it?"
                    ),
                ),
                (
                    "outcome_quality",
                    models.TextField(
                        help_text="Implementation Fidelity/Adherence/Quality. How will you be measuring it?"
                    ),
                ),
                (
                    "outcome_cost",
                    models.TextField(help_text="Cost. How will you keep track of it?"),
                ),
                (
                    "outcome_maintenance",
                    models.TextField(help_text="Maintenance/Sustainment."),
                ),
                (
                    "outcome_other",
                    models.TextField(help_text="Any other measures being planned?"),
                ),
                (
                    "implementation_completing_half",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="# (%) completing 50% of implementation strategy activities",
                        null=True,
                    ),
                ),
                (
                    "implementation_completing_majority",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="# (%) completing 80% or more of implementation strategy activities",
                        null=True,
                    ),
                ),
                (
                    "results_reach",
                    models.TextField(
                        blank=True,
                        help_text="Reach (# or percentage of population, what is the population, and how will you be measuring the outcome?",
                        null=True,
                    ),
                ),
                (
                    "results_effectiveness",
                    models.TextField(
                        blank=True,
                        help_text="Effectiveness of Intervention/Program/Services (w/consumers), how will you measure it?",
                        null=True,
                    ),
                ),
                (
                    "results_adoption",
                    models.TextField(
                        blank=True,
                        help_text="Results available for number of providers?",
                        null=True,
                    ),
                ),
                (
                    "results_quality",
                    models.TextField(
                        blank=True,
                        help_text="Results available for implementation Fidelity/Adherence/Quality?",
                        null=True,
                    ),
                ),
                (
                    "results_cost",
                    models.TextField(
                        blank=True, help_text="Results available for cost?", null=True
                    ),
                ),
                (
                    "results_maintenance",
                    models.TextField(
                        blank=True,
                        help_text="Results for Maintenance/Sustainment.",
                        null=True,
                    ),
                ),
                (
                    "results_other",
                    models.TextField(
                        blank=True, help_text="Results available for other?", null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Strategy",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "time_updated",
                    models.DateTimeField(auto_now=True, verbose_name="date modified"),
                ),
                ("frequency", models.CharField(help_text="Frequency", max_length=250)),
                (
                    "strategy_format",
                    models.CharField(
                        blank=True, help_text="Format", max_length=500, null=True
                    ),
                ),
                (
                    "strategy_type",
                    models.CharField(
                        blank=True, help_text="Type", max_length=500, null=True
                    ),
                ),
                (
                    "planned_number_units",
                    models.PositiveIntegerField(help_text="Planned number of units"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Training",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "time_updated",
                    models.DateTimeField(auto_now=True, verbose_name="date modified"),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("image_data", models.TextField(blank=True, null=True)),
                (
                    "image_url",
                    models.URLField(
                        blank=True,
                        help_text="Leave this blank to use the default template.",
                        max_length=500,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("dates", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "duration",
                    models.CharField(
                        blank=True,
                        help_text="duration with units (typically hours)",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "center",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="users.Center"
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "center")},
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "time_updated",
                    models.DateTimeField(auto_now=True, verbose_name="date modified"),
                ),
                ("name", models.CharField(max_length=250)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("stage", models.PositiveIntegerField(default=1)),
                (
                    "center",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="users.Center"
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "form",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.FormTemplate",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="formtemplate",
            name="implement_strategy",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="form_template1",
                related_query_name="form_template1",
                to="main.Strategy",
            ),
        ),
        migrations.CreateModel(
            name="TrainingParticipant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "training",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.Training"
                    ),
                ),
            ],
            options={
                "unique_together": {("email", "training")},
            },
        ),
    ]

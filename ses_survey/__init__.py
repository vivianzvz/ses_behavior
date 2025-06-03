from otree.api import *

class C(BaseConstants):
    NAME_IN_URL     = 'ses_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS      = 1
    ETHNICITIES = [
        "Hispanic/Latino/Spanish origin",
        "White",
        "Black or African American",
        "Asian",
        "Native American/Alaska Native",
        "Native Hawaiian/Pacific Islander",
        "Middle Eastern/North African",
        "Other",
    ]
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # Part 1: basic demographics
    age = models.IntegerField(label="What is your age?")
    gender = models.StringField(
        choices=["Man","Woman","Non-Binary","Other"],
        widget=widgets.RadioSelect,
        label="What is your gender?"
    )

    # One BooleanField per ethnicity:
    hispanic_latino_spanish_origin = models.BooleanField(
        label="Hispanic/Latino/Spanish origin", blank=True
    )
    white = models.BooleanField(label="White", blank=True)
    black_or_african_american = models.BooleanField(
        label="Black or African American", blank=True
    )
    asian = models.BooleanField(label="Asian", blank=True)
    native_american_alaska_native = models.BooleanField(
        label="Native American/Alaska Native", blank=True
    )
    native_hawaiian_pacific_islander = models.BooleanField(
        label="Native Hawaiian/Pacific Islander", blank=True
    )
    middle_eastern_north_african = models.BooleanField(
        label="Middle Eastern/North African", blank=True
    )
    other_ethnicity = models.BooleanField(label="Other", blank=True)

    college_year = models.StringField(
        choices=[
            "Freshman (<45 credits)",
            "Sophomore (45–89 credits)",
            "Junior (90–134 credits)",
            "Senior (135+ credits)"
        ],
        widget=widgets.RadioSelect,
        label="What year are you in college (credit-wise)?")

    # Part 2: current SES
    full_time_student = models.StringField(
        choices=["Full time","Part time"],
        widget=widgets.RadioSelect,
        label="Are you a full-time or part-time student?"
    )
    took_econ = models.StringField(
        choices=["Yes","No"],
        widget=widgets.RadioSelect,
        label="Have you taken economics classes?"
    )
    family_income = models.StringField(
        choices=[
            "$0–$19,999","$20,000–$49,999","$50,000–$74,999",
            "$75,000–$100,000","$100,000–$150,000","More than $150,000"
        ],
        widget=widgets.RadioSelect,
        label="What is your household’s combined annual income? (Give your best estimate)"
    )
    employment_status = models.StringField(
        choices=[
            "Full-time employment","Part-time employment",
            "Self-employed","Not currently employed","Other"
        ],
        widget=widgets.RadioSelect,
        label="What is your current employment status?"
    )
    personal_income = models.StringField(
        choices=[
            "$0–$19,999","$20,000–$49,999","$50,000–$74,999",
            "$75,000–$100,000","More than $100,000","Prefer not to say", "N/A"
        ],
        widget=widgets.RadioSelect,
        label="If employed, what is your personal annual income? Otherwise, choose 'N/A'"
    )
    has_assets = models.StringField(
        choices=["Yes","No","Prefer not to say"],
        widget=widgets.RadioSelect,
        label="Do you have any assets or investments (savings, real estate, etc.)?"
    )
    housing = models.StringField(
        choices=[
            "On-campus housing","Off-campus housing","Living with family","Other"
        ],
        widget=widgets.RadioSelect,
        label="Which best describes your current housing arrangement?"
    )
    gov_assistance = models.StringField(
        choices=["SNAP/EBT","Medicaid","Housing Assistance","Unemployment Benefits","None"],
        widget=widgets.RadioSelect,
        label="Do you receive any government assistance that's listed below (excluding financial aid)?"
    )

    # Part 3: childhood SES
    ladder_family = models.IntegerField(
        min=1, max=10,
        label=(
            "Imagine a 10-rung ladder. At the top (10) are households in your country that "
            "are the wealthiest; at the bottom (1) are households in your country that are the poorest. "
            "Where do you think your family currently stands?"
        )
    )
    ladder_self = models.IntegerField(
        min=1, max=10,
        label=(
            "Using the same ladder (1 = poorest, 10 = wealthiest), where do you think you personally stand?"
        )
    )
    childhood_zip = models.StringField(
        label="City & ZIP (or postal code) of your childhood residence (or 'Unsure')"
    )
    childhood_income = models.StringField(
        choices=[
            "$0–$19,999","$20,000–$49,999","$50,000–$74,999",
            "$75,000–$100,000","More than $100,000","Not sure"
        ],
        widget=widgets.RadioSelect,
        label="Approximate family income during childhood (ages 1–14)?"
    )
    childhood_assistance = models.StringField(
        choices=["Yes","No","Prefer not to say"],
        widget=widgets.RadioSelect,
        label="Did your family ever receive government assistance growing up?"
    )
    childhood_home_ownership = models.StringField(
        choices=["Yes","No","Prefer not to say"],
        widget=widgets.RadioSelect,
        label="Did your family own their home when you were growing up?"
    )

# INTRODUCTION PAGE
class SESIntro(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'progress_label':   "Introduction",
            'progress_percent': 1,
        }


# PAGES

class SESPage1(Page):
    form_model = 'player'
    # Include each BooleanField’s name explicitly:
    form_fields = [
        'age',
        'gender',
        'hispanic_latino_spanish_origin',
        'white',
        'black_or_african_american',
        'asian',
        'native_american_alaska_native',
        'native_hawaiian_pacific_islander',
        'middle_eastern_north_african',
        'other_ethnicity',
        'college_year',
    ]
    @staticmethod
    def vars_for_template(player):
        return {
            'progress_label':   f"Background Survey – Part 1",
            'progress_percent': 3.6,
        }

class SESPage2(Page):
    form_model = 'player'
    form_fields = [
        'full_time_student','took_econ',
        'family_income','employment_status','personal_income',
        'has_assets','housing','gov_assistance','ladder_family','ladder_self'
    ]
    @staticmethod
    def vars_for_template(player):
        return {
            'progress_label':   "Background Survey – Part 2",
            'progress_percent': 7.1,
        }

class SESPage3(Page):
    form_model = 'player'
    form_fields = [
        'childhood_zip','childhood_income','childhood_assistance','childhood_home_ownership'
    ]

    @staticmethod
    def before_next_page(player, timeout_happened):
        all_fields = (
            SESPage1.form_fields +
            SESPage2.form_fields +
            SESPage3.form_fields
        )
        for field in all_fields:
            # use field_maybe_none so that a None boolean doesn't trigger an error
            player.participant.vars[field] = player.field_maybe_none(field)
    @staticmethod
    def vars_for_template(player):
        return {
            'progress_label':   "Background Survey – Part 3",
            'progress_percent': 10.7,
        }
page_sequence = [SESIntro, SESPage1, SESPage2, SESPage3]

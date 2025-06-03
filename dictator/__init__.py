from otree.api import *



doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class C(BaseConstants):
    NAME_IN_URL = 'dictator'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    # Initial amount allocated to the dictator
    ENDOWMENT = cu(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0,
        max=C.ENDOWMENT,
        label="I will send",
    )


class Player(BasePlayer):
    pass


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = group.sent
    p2.payoff = C.ENDOWMENT - group.sent


# PAGES
class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label': f"Task 1 – Round 1",
            'progress_percent': 14.3,
        }


class Offer(Page):
    form_model = 'group'
    form_fields = ['sent']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label': f"Task 1 – Round 1",
            'progress_percent': 17.9,
        }

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label': f"Task 1 – Round 1",
            'progress_percent': 21.4,
        }

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'offer': player.group.sent,
            'progress_label': f"Task 1 – Round 1",
            'progress_percent': 25,
        }

page_sequence = [Introduction, Offer, ResultsWaitPage, Results]

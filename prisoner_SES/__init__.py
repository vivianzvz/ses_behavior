from otree.api import *

class C(BaseConstants):
    NAME_IN_URL       = 'prisoner_SES'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS        = 1
    PAYOFF_A          = cu(300)
    PAYOFF_B          = cu(200)
    PAYOFF_C          = cu(100)
    PAYOFF_D          = cu(0)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, 'Cooperate'], [False, 'Defect']],
        widget=widgets.RadioSelect,
        label="Your choice:"
    )


def other_player(player: Player):
    return player.get_others_in_group()[0]


def set_group_payoffs(group: Group):
    for p in group.get_players():
        o = p.cooperate
        q = other_player(p).cooperate
        matrix = {
            (False, True):  C.PAYOFF_A,
            (True,  True):  C.PAYOFF_B,
            (False, False): C.PAYOFF_C,
            (True,  False): C.PAYOFF_D
        }
        p.payoff = matrix[(o, q)]


# PAGES

class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label':   f"Task 3 – Round 2",
            'progress_percent': 89.3,
        }


class Decision(Page):
    form_model = 'player'
    form_fields = ['cooperate']

    @staticmethod
    def vars_for_template(player: Player):
        partner = other_player(player)
        ses     = partner.participant.vars
        return {
            'partner_personal_income': ses.get('personal_income'),
            'partner_family_income':   ses.get('family_income'),
            'partner_ladder_self':     ses.get('ladder_self'),
            'partner_gov_assistance':  ses.get('gov_assistance'),
            'progress_label':          f"Task 3 – Round 2",
            'progress_percent':        92.9,
        }


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_group_payoffs

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label':   f"Task 3 – Round 2",
            'progress_percent': 96.4,
        }


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        opponent = other_player(player)
        return {
            'my_decision':       'Cooperate' if player.cooperate else 'Defect',
            'opponent_decision': 'Cooperate' if opponent.cooperate else 'Defect',
            'same_choice':       player.cooperate == opponent.cooperate,
            'progress_label':    f"Task 3 – Round 2",
            'progress_percent':  100,
        }


page_sequence = [Introduction, Decision, ResultsWaitPage, Results]

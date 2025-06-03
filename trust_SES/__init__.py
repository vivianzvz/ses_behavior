from otree.api import *

class C(BaseConstants):
    NAME_IN_URL       = 'trust_SES'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS        = 1
    ENDOWMENT         = cu(100)
    MULTIPLIER        = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount      = models.CurrencyField(min=0, max=C.ENDOWMENT)
    sent_back_amount = models.CurrencyField(min=cu(0))


class Player(BasePlayer):
    pass


def set_payoffs(group: Group):
    p1, p2 = group.get_players()
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount


# PAGES

class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label':   f"Task 2 – Round 2",
            'progress_percent': 67.9,
        }


class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    @staticmethod
    def vars_for_template(player: Player):
        partner = player.group.get_player_by_id(2)
        ses     = partner.participant.vars
        return {
            'partner_personal_income': ses.get('personal_income'),
            'partner_family_income':   ses.get('family_income'),
            'partner_ladder_self':     ses.get('ladder_self'),
            'partner_gov_assistance':  ses.get('gov_assistance'),
            'progress_label':          f"Task 2 – Round 2",
            'progress_percent':        71.4,
        }


class SendBackWaitPage(WaitPage):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label':   f"Task 2 – Round 2",
            'progress_percent': 75.0,
        }


class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        partner = player.group.get_player_by_id(1)
        ses     = partner.participant.vars
        tripled = player.group.sent_amount * C.MULTIPLIER
        return {
            'partner_personal_income': ses.get('personal_income'),
            'partner_family_income':   ses.get('family_income'),
            'partner_ladder_self':     ses.get('ladder_self'),
            'partner_gov_assistance':  ses.get('gov_assistance'),
            'tripled_amount':          tripled,
            'progress_label':          f"Task 2 – Round 2",
            'progress_percent':        78.6,
        }


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'progress_label':   f"Task 2 – Round 2",
            'progress_percent': 82.1,
        }


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'tripled_amount':     player.group.sent_amount * C.MULTIPLIER,
            'endowment':          C.ENDOWMENT,
            'progress_label':     f"Task 2 – Round 2",
            'progress_percent':   85.7,
        }


page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]

from otree.api import *

class C(BaseConstants):
    NAME_IN_URL       = 'dictator_SES'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS        = 1
    ENDOWMENT         = cu(100)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    offer = models.CurrencyField(min=0, max=C.ENDOWMENT)

class Offer(Page):
    form_model = 'player'
    form_fields = ['offer']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

    @staticmethod
    def vars_for_template(player):
        # Grab Player 2’s SES from participant.vars
        partner = player.group.get_player_by_id(2)
        ses     = partner.participant.vars

        return {
            'partner_personal_income': ses.get('personal_income'),
            'partner_family_income':   ses.get('family_income'),
            'partner_ladder_self':     ses.get('ladder_self'),
            'partner_gov_assistance':  ses.get('gov_assistance'),
            'progress_label':          f"Task 1 – Round 2",
            'progress_percent':        64.3,
        }


page_sequence = [Offer]

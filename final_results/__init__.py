from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'final_results'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession): pass
class Group(BaseGroup): pass
class Player(BasePlayer): pass

class FinalResults(Page):

    @staticmethod
    def vars_for_template(player):
        payoff_in_dollars = player.participant.payoff.to_real_world_currency(player.session)
        show_up_fee = player.session.config['participation_fee']
        conversion_rate = player.session.config['real_world_currency_per_point']
        total_payment = payoff_in_dollars + show_up_fee
        return {
            'total_payoff': player.participant.payoff,
            'conversion_rate': conversion_rate,
            'show_up_fee': show_up_fee,
            'total_payment': total_payment,
        }

page_sequence = [FinalResults]

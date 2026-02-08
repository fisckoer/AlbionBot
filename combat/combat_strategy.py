
class CombatStrategy:
    """
    Estrategia básica: atacar siempre.
    """

    def next_action(self, state):
        #if not state.has_target:
        #    return "ACQUIRE_TARGET"

        return "BASIC_ATTACK"

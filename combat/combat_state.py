from dataclasses import dataclass

@dataclass
class CombatState:
    in_combat: bool
    hp_percent: int
    #has_target: bool
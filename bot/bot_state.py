
class BotState:
    is_farming = False
    is_in_combat = False
    is_escaping = False
    stop_movement = False
    is_mount =True
    is_mounting = False
    running = True
    request_farming = False
    moob_watch =False

    def __str__(self) -> str:
        return (
            "BotState(\n"
            f"  is_farming      = {self.is_farming}\n"
            f"  is_in_combat    = {self.is_in_combat}\n"
            f"  is_escaping     = {self.is_escaping}\n"
            f"  stop_movement   = {self.stop_movement}\n"
            f"  is_mount        = {self.is_mount}\n"
            f"  is_mounting     = {self.is_mounting}\n"
            f"  running         = {self.running}\n"
            f"  request_farming = {self.request_farming}\n"
            ")"
        )
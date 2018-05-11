
class GameStatusConstants(object):
    WAITING_REGISTRATIONS_OPENING = 'WAITING_REGISTRATIONS_OPENING'
    WAITING_PLAYERS = 'WAITING_PLAYERS'
    WAITING_GAME_LAUNCH = 'WAITING_GAME_LAUNCH'
    WAITING_PLAYER_INPUT = 'WAITING_PLAYER_INPUT'
    PROCESSING_PLAYER_INPUT = 'PROCESSING_PLAYER_INPUT'
    PLAYER_WINS = 'PLAYER_WINS'
    FINISHED = 'FINISHED'

    @property
    def default(self):
        return self.WAITING_REGISTRATIONS_OPENING

    def getNext(self, status):
        if status == self.WAITING_REGISTRATIONS_OPENING:
            return self.WAITING_PLAYERS
        if status == self.WAITING_PLAYERS:
            return self.WAITING_GAME_LAUNCH
        if status == self.WAITING_GAME_LAUNCH:
            return self.WAITING_PLAYER_INPUT
        if status == self.WAITING_PLAYER_INPUT:
            return self.PROCESSING_PLAYER_INPUT
        if status == self.PROCESSING_PLAYER_INPUT:
            return self.PLAYER_WINS
        if status == self.PLAYER_WINS:
            return self.FINISHED
        if status == self.FINISHED:
            return self.FINISHED
        else:
            return self.WAITING_REGISTRATIONS_OPENING

    def as_list(self):
        return [
            self.WAITING_REGISTRATIONS_OPENING,
            self.WAITING_PLAYERS,
            self.WAITING_GAME_LAUNCH,
            self.WAITING_PLAYER_INPUT,
            self.PROCESSING_PLAYER_INPUT,
            self.PLAYER_WINS,
            self.FINISHED,
        ]

    def as_list_labels(self):
        return ''.join('%s,' % _ for _ in self.as_list())

    def as_choices(self):
        return list().extend((_, _) for _ in self.as_list())


class GameGenreConstants(object):
    HF = 'HF'
    FH = 'FH'
    HH = 'HH'
    FF = 'FF'

    @property
    def default(self):
        return self.HF

    def as_list(self):
        return [
            self.HF,
            self.FH,
            self.HH,
            self.FF,
        ]

    def as_list_labels(self):
        return ''.join('%s,' % _ for _ in self.as_list())

    def as_choices(self):
        return list().extend((_, _) for _ in self.as_list())


GAME_STATUS = GameStatusConstants()
GAME_GENRES = GameGenreConstants()

class Cricket:
    def __init__(self,players,scores):
        self.players = players
        self.scores = scores
    def TeamIndia(self):
        print("The team India player:{}\nscores:{}".format(self.players,self.scores))
match1 =Cricket("msd",200)
match2 =Cricket("Koholi",300)
match1.TeamIndia()
match2.TeamIndia()
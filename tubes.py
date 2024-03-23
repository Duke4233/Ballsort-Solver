class tube:
    def __init__(self, size, balls,id):
        self.balls = balls
        self.size = size
        self.top = self.balls[0]
        self.full = (len(self.balls) == 4)
        self.id = id
    def is_solved(self):
        for ball in self.balls:
            if not ball.solved:
                return False

    

class tube:
    def __init__(self, size, tube_id):
        self.balls = []
        self.size = size
        self.top = None
        self.full = (len(self.balls) == 4)
        self.id = tube_id

    def is_solved(self):
        last_ball = self.balls[0]
        for ball in self.balls:
            if ball.color != last_ball.color:
                return False

    def pop_top(self):
        poping_ball = self.balls.pop(0)
        self.top = self.balls[-1]
        return poping_ball

    def add_ball(self, ball_to_add):
        if not self.full:
            self.balls.append(ball_to_add)
            self.top = self.balls[-1]
            return True
        return False

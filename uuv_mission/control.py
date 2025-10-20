class PDController:
    """Discrete-time PD: u[t] = Kp*e[t] + Kd*(e[t]-e[t-1])"""
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0.0

    def reset(self): self.prev_error = 0.0

    def __call__(self, r: float, y: float) -> float:
        e = r - y
        de = e - self.prev_error
        u = self.kp * e + self.kd * de
        self.prev_error = e
        return float(u)

class Tween:
    def __init__(self, init_val, final_val, dt, interpolation_method: str):
        self.init_val = init_val
        self.final_val = final_val
        self.dt = dt
        self.interpolation_method = interpolation_method

    def get_val(self, t):
        if self.interpolation_method == "linear":
            pass
        elif self.interpolation_method == "quadratic":
            pass
        elif self.interpolation_method == "logistic":
            pass
        elif self.interpolation_method == "bounce":
            pass
        else:
            return self.final_val

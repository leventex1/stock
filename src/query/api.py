

class APIParams:

    def to_dict(self):
        return {
            k: v for k, v in vars(self).items()
            if v is not None  
        }
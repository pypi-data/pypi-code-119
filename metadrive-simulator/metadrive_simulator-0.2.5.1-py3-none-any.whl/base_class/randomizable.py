from metadrive.utils.random_utils import get_np_random


class Randomizable:
    """
    Global Random Engine serving as the super class of BaseManager, it can sync all seeds in all managers automatically
    Then all objects generated by XxxManager will be set a random seed by GlobalRandomEngine.randint().
    In the lifetime of GlobalRandomEngine's subclasses, these instances will be seeded for several times
    """
    MAX_RAND_INT = 65536

    def __init__(self, random_seed):
        self.random_seed = random_seed
        self.np_random = get_np_random(self.random_seed)

    def seed(self, random_seed):
        self.random_seed = random_seed
        self.np_random = get_np_random(random_seed)

    def generate_seed(self):
        return self.np_random.randint(0, self.MAX_RAND_INT)

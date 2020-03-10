class Integrator():
    """Inegrator class which stores integrator information

    Attributes:
        name: {str} -- name of the integrator technique
        maxdepth: {int} -- maximum number of bounds
    """

    def __init__(self, name, maxdepth):
        """Construct Sampler instance
        
        Arguments:
            name: {str} -- name of the integrator technique
            maxdepth: {int} -- maximum number of bounds
        """
        self.name = name
        self.maxdepth = int(maxdepth)

    def __str__(self):
        """Display Integrator information
        
        Returns:
            {str} -- Integrator information
        """
        return "Integrator: `{0}` with max depth {1}".format(
            self.name, self.maxdepth)
class Sampler():
    """Sampler class representation
        
    Attributes:
        name: {str} -- name of the sampler technique
        pixelsamples: {int} -- number of samples used
    """

    def __init__(self, name, pixelsamples):
        """Construct Sampler instance
        
        Arguments:
            name: {str} -- name of the sampler technique
            pixelsamples: {int} -- number of samples used
        """
        self.name = name
        self.pixelsamples = int(pixelsamples)

    def __str__(self):
        """Display Sampler information
        
        Returns:
            {str} Sampler information
        """
        return "Sampler: `{0}` with {1} samples per pixel".format(
            self.name, self.pixelsamples)
from zope.interface import Interface as I


class IChecksummable(I):
    """ an object for which a checksum can be obtained """


class IChecksumContent(I):
    """ retrieve content to be checksummed """


class IChecksumStorage(I):
    """ retrieve content to be checksummed """


class IChecksum(I):
    """ The checksum of an object """

    def calculate(self):
        pass

    def update(self):
        pass

    def compare(self):
        pass

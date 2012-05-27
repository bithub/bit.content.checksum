import hashlib

from zope.interface import implements
from zope.annotation.interfaces import IAnnotations

from bit.content.checksum.interfaces\
    import IChecksum, IChecksumContent, IChecksumStorage
from bit.content.checksum import CHECKSUM_STORAGE


class ChecksumStorage(object):
    implements(IChecksumStorage)

    def __init__(self, context):
        self.context = context

    def get_checksum(self):
        return IAnnotations(self.context).get(CHECKSUM_STORAGE) or None

    def set_checksum(self, checksum):
        IAnnotations(self.context)[CHECKSUM_STORAGE] = checksum

    checksum = property(get_checksum, set_checksum)


class Checksum(object):
    implements(IChecksum)

    def __init__(self, context):
        self.context = context

    @property
    def checksum(self):
        storage = IChecksumStorage(self.context, None)
        if storage and storage.checksum is not None:
            return storage.checksum
        return self.update()

    def update(self):
        storage = IChecksumStorage(self.context, None)
        checksum = self.calculate()
        if storage:
            storage.checksum = checksum
        return checksum

    def calculate(self):
        content = IChecksumContent(self.context).content
        m = hashlib.md5()
        m.update(content)
        return m.hexdigest()

    def verify(self):
        storage = IChecksumStorage(self.context, None)
        if storage and storage.checksum is not None:
            return storage.checksum == self.calculate()
        return True

    def compare(self, obj):
        return self.checksum == IChecksum(obj).checksum

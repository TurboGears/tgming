from ming import schema as s
from ming.orm import FieldProperty, RelationProperty
from ming.orm.property import ORMProperty, LazyProperty, OneToManyJoin
from pymongo.objectid import ObjectId

class SynonymProperty(ORMProperty):
    include_in_repr = True

    def __init__(self, getter, setter=None):
        super(ORMProperty, self).__init__()
        self.getter = getter
        self.setter = setter

    def __get__(self, instance, cls=None):
        if not instance:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        if not self.setter:
            raise TypeError, 'read-only property'
        else:
            self.setter(instance, value)

    def repr(self, doc):
        return repr(self)

    def __repr__(self):
        return '<%s>' % (self.__class__.__name__,)

class ProgrammaticRelationProperty(RelationProperty):
    include_in_repr = False

    def __init__(self, related, getter, setter=None, relation_field=None):
        super(ProgrammaticRelationProperty, self).__init__(related)
        self.relation_field = relation_field
        self.getter = getter
        self.setter = setter

    def __get__(self, instance, cls=None):
        if not instance:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        if not self.setter:
            raise TypeError, 'read-only property'
        else:
            self.setter(instance, value)

    @LazyProperty
    def join(self):
        return OneToManyJoin(self.mapper.mapped_class, self.related, self.relation_field)


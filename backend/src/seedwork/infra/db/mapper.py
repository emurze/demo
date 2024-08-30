import abc


class IDataMapper[Entity, Model](abc.ABC):
    @abc.abstractmethod
    def entity_to_model(self, entity: Entity) -> Model: ...

    @abc.abstractmethod
    def model_to_entity(self, model: Model) -> Entity: ...

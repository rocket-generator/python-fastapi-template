from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Optional

from injector import Injector, inject
from sqlalchemy import and_
from sqlalchemy.orm import scoped_session

from ..interfaces.repositories.base_repository_interface import \
    BaseRepositoryInterface
from ..models import Base


class BaseRepository(BaseRepositoryInterface, metaclass=ABCMeta):

    @property
    @abstractmethod
    def model(self):
        raise NotImplementedError

    @inject
    def __init__(self, db: scoped_session):
        self._db = db

    def list(self, offset: int = 0, limit: int = 20) -> List[model]:
        return self._db.query(self.model).limit(limit).offset(offset).all()

    def list_by_filter(self,
                       _filter: dict,
                       offset: int = 0,
                       limit: int = 20) -> List[model]:
        query = self._db.query(self.model)

        filter_conditions = []
        for key, value in _filter.items():
            if hasattr(self.model, key):
                filter_conditions.append(getattr(self.model, key) == value)

        if filter_conditions:
            query = query.filter(and_(*filter_conditions))

        return query.limit(limit).offset(offset).all()

    def get_by_id(self, _id: str) -> model:
        return self._db.query(self.model).filter(self.model.id == _id).first()

    def create(self, data: Dict[str, Any]) -> model:
        instance = self.model(**data)
        self._db.add(instance)
        self._db.commit()
        return instance

    def update(self, _id: str, data: Dict[str, Any]) -> model:
        instance = self.get_by_id(_id)
        if instance:
            for key, value in data.items():
                setattr(instance, key, value)
            self._db.commit()
        return instance

    def delete(self, _id: str) -> None:
        instance = self.get_by_id(_id)
        if instance:
            self._db.delete(instance)
            self._db.commit()

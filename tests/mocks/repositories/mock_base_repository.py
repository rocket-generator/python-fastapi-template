from typing import Any, Dict, List, Optional

from app.interfaces.repositories.base_repository_interface import \
    BaseRepositoryInterface
from app.models.admin_user import AdminUser
from tests.mocks.model_factories.admin_user import admin_user_factory


class MockBaseRepository(BaseRepositoryInterface):

    @property
    def model(self):
        raise NotImplementedError

    def generate_model(self,
                       _id: Optional[str] = None,
                       data: Optional[dict] = None) -> model:
        raise NotImplementedError

    def list(self, offset: int = 0, limit: int = 20) -> List[model]:
        model = self.generate_model()
        return [model]

    def list_by_filter(self,
                       _filter: dict,
                       offset: int = 0,
                       limit: int = 20) -> List[model]:
        return self.list(offset, limit)

    def get_by_id(self, _id: str) -> Optional[Any]:
        return self.generate_model(_id=_id)

    def create(self, data: Dict[str, Any]) -> Any:
        return self.generate_model(data=data)

    def update(self, _id: str, data: Dict[str, Any]) -> Optional[Any]:
        model = self.get_by_id(_id)
        if model:
            for key, value in data.items():
                setattr(model, key, value)
        return model

    def delete(self, _id: str) -> None:
        pass

"""create_admin_users

Revision ID: 202406090901
Revises:
Create Date: 2024-06-09 09:16:51.483252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy
from sqlalchemy.sql import func, text


# revision identifiers, used by Alembic.
revision: str = '202406090901'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# uuid_blob(uuid())
# gen_random_uuid()

def upgrade() -> None:
    op.create_table(
        'admin_users',
        sqlalchemy.Column('id', sqlalchemy.Uuid, primary_key=True, server_default=text('gen_random_uuid()')),
        sqlalchemy.Column('name', sqlalchemy.Text, nullable=False),
        sqlalchemy.Column('email', sqlalchemy.Text, nullable=False),
        sqlalchemy.Column('password', sqlalchemy.Text, nullable=False),

        sqlalchemy.Column('created_at', sqlalchemy.TIMESTAMP(timezone=True), nullable=False,
                          server_default=func.now()),
        sqlalchemy.Column('updated_at', sqlalchemy.TIMESTAMP(timezone=True), nullable=False,
                          server_default=func.now(),
                          onupdate=func.now()),
    )

    op.create_index('admin_users_email', 'admin_users', ['email'])


def downgrade() -> None:
    op.drop_table('admin_users')

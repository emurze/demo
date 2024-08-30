"""empty message

Revision ID: 42e4dce7c6a0
Revises: e8d03eaa750a
Create Date: 2024-08-21 18:52:35.255247

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "42e4dce7c6a0"
down_revision: Union[str, None] = "e8d03eaa750a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""empty message

Revision ID: e8d03eaa750a
Revises: 0fa992852268
Create Date: 2024-08-21 15:32:53.428956

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e8d03eaa750a"
down_revision: Union[str, None] = "0fa992852268"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

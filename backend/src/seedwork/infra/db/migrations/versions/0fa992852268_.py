"""empty message

Revision ID: 0fa992852268
Revises: 9667553a5f42
Create Date: 2024-08-21 15:25:17.312468

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0fa992852268"
down_revision: Union[str, None] = "9667553a5f42"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

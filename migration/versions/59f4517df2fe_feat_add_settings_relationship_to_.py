"""feat: add Settings relationship to PublishArticleStatus - 3

Revision ID: 59f4517df2fe
Revises: 0c4503ffeb72
Create Date: 2023-12-24 18:15:33.589355

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "59f4517df2fe"
down_revision: Union[str, None] = "0c4503ffeb72"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "publisharticlestatus",
        sa.Column(
            "status",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=False,
            server_default="PENDING",
        ),
    )
    op.execute("UPDATE publisharticlestatus SET status = publish_status")
    op.drop_column("publisharticlestatus", "publish_status")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "publisharticlestatus",
        sa.Column(
            "publish_status", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.drop_column("publisharticlestatus", "status")
    # ### end Alembic commands ###
"""init: models

Revision ID: 4ee7851ec8a4
Revises:
Create Date: 2023-12-21 16:27:32.179647

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4ee7851ec8a4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "project",
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("url", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "parse_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("parse_last_material", sa.Integer(), nullable=False),
        sa.Column("parse_material_id_element", sa.JSON(), nullable=True),
        sa.Column("parse_material_url_element", sa.JSON(), nullable=True),
        sa.Column("parse_material_img_element", sa.JSON(), nullable=True),
        sa.Column("parse_material_body_element", sa.JSON(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "url", name="unique_name_url"),
    )
    op.create_foreign_key(None, "setting", "project", ["project_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "setting", type_="foreignkey")
    op.drop_table("project")
    # ### end Alembic commands ###
"""Altera os tipos datetime para date

Revision ID: 4cef5c740ec4
Revises: 3e3c4ee43712
Create Date: 2024-12-27 19:54:55.511059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4cef5c740ec4'
down_revision: Union[str, None] = '3e3c4ee43712'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contas_a_pagar_e_receber', 'data_previsao',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
    op.alter_column('contas_a_pagar_e_receber', 'data_baixa',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contas_a_pagar_e_receber', 'data_baixa',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('contas_a_pagar_e_receber', 'data_previsao',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    # ### end Alembic commands ###
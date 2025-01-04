"""Adiciona colunas de controle de baixa de uma conta

Revision ID: 98133e1e8f96
Revises: 163b33efd561
Create Date: 2024-12-03 09:48:54.094510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98133e1e8f96'
down_revision: Union[str, None] = '163b33efd561'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contas_a_pagar_e_receber', sa.Column('data_baixa', sa.DateTime(), nullable=True))
    op.add_column('contas_a_pagar_e_receber', sa.Column('valor_baixa', sa.Numeric(), nullable=True))
    op.add_column('contas_a_pagar_e_receber', sa.Column('esta_baixada', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contas_a_pagar_e_receber', 'esta_baixada')
    op.drop_column('contas_a_pagar_e_receber', 'valor_baixa')
    op.drop_column('contas_a_pagar_e_receber', 'data_baixa')
    # ### end Alembic commands ###
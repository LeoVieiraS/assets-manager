"""empty message

Revision ID: e626229a71df
Revises: 
Create Date: 2022-10-05 14:51:05.009753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e626229a71df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('operation_type', sa.String(), nullable=False),
    sa.Column('asset', sa.String(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('peer_coin', sa.String(), nullable=False),
    sa.Column('peer_coin_total_value', sa.Float(), nullable=False),
    sa.Column('type_value', sa.String(), nullable=False),
    sa.Column('usd_total_value', sa.Float(), nullable=False),
    sa.Column('usd_unit_price', sa.Float(), nullable=False),
    sa.Column('fee', sa.Float(), nullable=False),
    sa.Column('usd_fee', sa.Float(), nullable=False),
    sa.Column('coin_fee', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    # ### end Alembic commands ###
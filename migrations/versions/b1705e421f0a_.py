"""empty message

Revision ID: b1705e421f0a
Revises: 2ca97b4bbbd5
Create Date: 2023-11-27 10:36:34.276138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1705e421f0a'
down_revision = '2ca97b4bbbd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], name=op.f('fk_carts_movie_id_movies')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_carts_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carts')
    # ### end Alembic commands ###

"""empty message

Revision ID: f1318346a431
Revises: None
Create Date: 2016-01-30 16:42:51.170407

"""

# revision identifiers, used by Alembic.
revision = 'f1318346a431'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_gdg_help_desk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('help_title', sa.String(length=200), nullable=True),
    sa.Column('help_content', sa.Text(), nullable=True),
    sa.Column('author_address', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_gdg_help_desk')
    ### end Alembic commands ###

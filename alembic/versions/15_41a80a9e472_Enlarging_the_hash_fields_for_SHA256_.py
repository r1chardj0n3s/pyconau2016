"""Enlarging the hash fields for SHA-256

Revision ID: 41a80a9e472
Revises: 436760a3036b
Create Date: 2015-05-02 17:01:08.559310

"""

# revision identifiers, used by Alembic.
revision = '41a80a9e472'
down_revision = '436760a3036b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person', u'password_hash',
                    existing_type=sa.TEXT(),
                    type_=sa.String(length=64))
    op.alter_column('person', u'url_hash',
                    existing_type=sa.String(length=32),
                    type_=sa.String(length=64))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('person', u'password_hash',
                    existing_type=sa.String(length=64),
                    type_=sa.TEXT())
    op.alter_column('person', u'url_hash',
                    existing_type=sa.String(length=64),
                    type_=sa.String(length=32))
    ### end Alembic commands ###

"""empty message

Revision ID: 65c0c869386c
Revises: b12b3bab2d85
Create Date: 2022-02-06 13:07:10.804099

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '65c0c869386c'
down_revision = 'b12b3bab2d85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uploads',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('sound_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sound_id'], ['sounds.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'sound_id')
    )
    op.add_column('sounds', sa.Column('audiofile', sa.LargeBinary(), nullable=False))
    op.drop_constraint('sounds_uploader_fkey', 'sounds', type_='foreignkey')
    op.drop_column('sounds', 'sound_file')
    op.drop_column('sounds', 'uploader')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sounds', sa.Column('uploader', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('sounds', sa.Column('sound_file', postgresql.BYTEA(), autoincrement=False, nullable=False))
    op.create_foreign_key('sounds_uploader_fkey', 'sounds', 'users', ['uploader'], ['id'])
    op.drop_column('sounds', 'audiofile')
    op.drop_table('uploads')
    # ### end Alembic commands ###

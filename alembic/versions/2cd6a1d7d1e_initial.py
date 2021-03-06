"""Initial

Revision ID: 2cd6a1d7d1e
Revises: None
Create Date: 2014-04-01 15:08:11.016314

"""

# revision identifiers, used by Alembic.
revision = '2cd6a1d7d1e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('hashkey'),
    sa.UniqueConstraint('username')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('useritem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plugins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['useritem.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey'),
    sa.UniqueConstraint('name')
    )
    op.create_table('authorization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('oauth_token', sa.String(length=255), nullable=True),
    sa.Column('oauth_token_secret', sa.String(length=255), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('expires_in', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'name')
    )
    op.create_table('metrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['useritem.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['useritem.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey'),
    sa.UniqueConstraint('name')
    )
    op.create_table('userprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('timezone', sa.Text(), nullable=True),
    sa.Column('settings', sa.JSONEncodedDict(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('groupprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('timezone', sa.Text(), nullable=True),
    sa.Column('settings', sa.JSONEncodedDict(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_plugins',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('plugin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plugin_id'], ['plugins.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('group_plugins',
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('plugin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['plugin_id'], ['plugins.id'], )
    )
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('scope', sa.String(length=255), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey')
    )
    op.create_table('user_metrics',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('metric_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['metric_id'], ['metrics.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('pluginmodels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.Column('plugin_id', sa.String(length=255), nullable=True),
    sa.Column('metric_id', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['metric_id'], ['metrics.name'], ),
    sa.ForeignKeyConstraint(['plugin_id'], ['plugins.hashkey'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey'),
    sa.UniqueConstraint('metric_id', 'plugin_id'),
    sa.UniqueConstraint('name', 'plugin_id')
    )
    op.create_table('user_sources',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['source_id'], ['sources.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('user_groups',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('resourcedata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.Column('settings', sa.JSONEncodedDict(), nullable=True),
    sa.Column('author_email', sa.Text(), nullable=True),
    sa.Column('current_view', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey')
    )
    op.create_table('pluginviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.Column('plugin_id', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['plugin_id'], ['plugins.hashkey'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hashkey'),
    sa.UniqueConstraint('name', 'plugin_id')
    )
    op.create_table('resource_views',
    sa.Column('resourcedata_id', sa.Integer(), nullable=True),
    sa.Column('pluginview_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pluginview_id'], ['pluginviews.id'], ),
    sa.ForeignKeyConstraint(['resourcedata_id'], ['resourcedata.id'], )
    )
    op.create_table('resource_permissions',
    sa.Column('resourcedata_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['resourcedata_id'], ['resourcedata.id'], )
    )
    op.create_table('plugindata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plugin_id', sa.String(length=255), nullable=True),
    sa.Column('metric_id', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.String(length=255), nullable=True),
    sa.Column('plugin_model_id', sa.String(length=255), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('data', sa.JSONEncodedDict(), nullable=True),
    sa.Column('hashkey', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['metric_id'], ['metrics.name'], ),
    sa.ForeignKeyConstraint(['plugin_id'], ['plugins.hashkey'], ),
    sa.ForeignKeyConstraint(['plugin_model_id'], ['pluginmodels.hashkey'], ),
    sa.ForeignKeyConstraint(['source_id'], ['sources.name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plugin_id', 'metric_id', 'user_id', 'hashkey')
    )
    op.create_table('resource_related',
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('related_id', sa.Integer(), nullable=True),
    sa.Column('col', sa.Integer(), nullable=True),
    sa.Column('row', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['resourcedata.id'], ),
    sa.ForeignKeyConstraint(['related_id'], ['resourcedata.id'], )
    )
    op.create_table('resourcelayout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resourcedata_id', sa.Integer(), nullable=True),
    sa.Column('sizeX', sa.Integer(), nullable=True),
    sa.Column('sizeY', sa.Integer(), nullable=True),
    sa.Column('row', sa.Integer(), nullable=True),
    sa.Column('col', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resourcedata_id'], ['resourcedata.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resourcelayout')
    op.drop_table('resource_related')
    op.drop_table('plugindata')
    op.drop_table('resource_permissions')
    op.drop_table('resource_views')
    op.drop_table('pluginviews')
    op.drop_table('resourcedata')
    op.drop_table('user_groups')
    op.drop_table('user_sources')
    op.drop_table('pluginmodels')
    op.drop_table('user_metrics')
    op.drop_table('permissions')
    op.drop_table('group_plugins')
    op.drop_table('user_plugins')
    op.drop_table('groupprofile')
    op.drop_table('roles_users')
    op.drop_table('groups')
    op.drop_table('userprofile')
    op.drop_table('sources')
    op.drop_table('metrics')
    op.drop_table('authorization')
    op.drop_table('plugins')
    op.drop_table('useritem')
    op.drop_table('role')
    op.drop_table('user')
    ### end Alembic commands ###

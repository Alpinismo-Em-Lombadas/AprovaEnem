"""migration inicial vazia

Revision ID: 219165086a1b
Revises:
Create Date: 2026-10-17 16:26:07.575092

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "219165086a1b"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

"""empty message

Revision ID: 47c0338ee9ff
Revises: 2a189257dcab
Create Date: 2020-04-18 15:41:33.112953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "47c0338ee9ff"
down_revision = "2a189257dcab"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "fk_class_translation_class_id_class", "class_translation", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_class_translation_class_id_class"),
        "class_translation",
        "class",
        ["class_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_custom_set_stats_custom_set_id_custom_set",
        "custom_set_stat",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_custom_set_stat_custom_set_id_custom_set"),
        "custom_set_stat",
        "custom_set",
        ["custom_set_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_equipped_item_custom_set_id_custom_set", "equipped_item", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_equipped_item_item_id_item", "equipped_item", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_equipped_item_item_slot_id_item_slot", "equipped_item", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_equipped_item_item_slot_id_item_slot"),
        "equipped_item",
        "item_slot",
        ["item_slot_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        op.f("fk_equipped_item_custom_set_id_custom_set"),
        "equipped_item",
        "custom_set",
        ["custom_set_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        op.f("fk_equipped_item_item_id_item"),
        "equipped_item",
        "item",
        ["item_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_equipped_item_exo_equipped_item_id_equipped_item",
        "equipped_item_exo",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_equipped_item_exo_equipped_item_id_equipped_item"),
        "equipped_item_exo",
        "equipped_item",
        ["equipped_item_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint("fk_item_item_type_id_item_type", "item", type_="foreignkey")
    op.drop_constraint("fk_item_set_id_set", "item", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_item_set_id_set"),
        "item",
        "set",
        ["set_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        op.f("fk_item_item_type_id_item_type"),
        "item",
        "item_type",
        ["item_type_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_item_stat_translation_item_stat_id_item_stat",
        "item_stat_translation",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_item_stat_translation_item_stat_id_item_stat"),
        "item_stat_translation",
        "item_stat",
        ["item_stat_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_item_translation_item_id_item", "item_translation", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_item_translation_item_id_item"),
        "item_translation",
        "item",
        ["item_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_item_type_slot_item_slot_id_item_slot", "item_type_slot", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_item_type_slot_item_type_id_item_type", "item_type_slot", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_item_type_slot_item_type_id_item_type"),
        "item_type_slot",
        "item_type",
        ["item_type_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        op.f("fk_item_type_slot_item_slot_id_item_slot"),
        "item_type_slot",
        "item_slot",
        ["item_slot_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_set_translation_set_id_set", "set_translation", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_set_translation_set_id_set"),
        "set_translation",
        "set",
        ["set_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_spell_spell_variant_pair_id_spell_variant_pair", "spell", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_spell_spell_variant_pair_id_spell_variant_pair"),
        "spell",
        "spell_variant_pair",
        ["spell_variant_pair_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_spell_effect_spell_stat_id_spell_stats", "spell_effect", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_spell_effect_spell_stat_id_spell_stats"),
        "spell_effect",
        "spell_stats",
        ["spell_stat_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_spell_stats_spell_id_spell", "spell_stats", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_spell_stats_spell_id_spell"),
        "spell_stats",
        "spell",
        ["spell_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_spell_variant_pair_class_id_class", "spell_variant_pair", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_spell_variant_pair_class_id_class"),
        "spell_variant_pair",
        "class",
        ["class_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_weapon_effect_weapon_stat_id_weapon_stat",
        "weapon_effect",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_weapon_effect_weapon_stat_id_weapon_stat"),
        "weapon_effect",
        "weapon_stat",
        ["weapon_stat_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.drop_constraint("fk_weapon_stat_item_id_item", "weapon_stat", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_weapon_stat_item_id_item"),
        "weapon_stat",
        "item",
        ["item_id"],
        ["uuid"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_weapon_stat_item_id_item"), "weapon_stat", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_weapon_stat_item_id_item", "weapon_stat", "item", ["item_id"], ["uuid"]
    )
    op.drop_constraint(
        op.f("fk_weapon_effect_weapon_stat_id_weapon_stat"),
        "weapon_effect",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_weapon_effect_weapon_stat_id_weapon_stat",
        "weapon_effect",
        "weapon_stat",
        ["weapon_stat_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_spell_variant_pair_class_id_class"),
        "spell_variant_pair",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_spell_variant_pair_class_id_class",
        "spell_variant_pair",
        "class",
        ["class_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_spell_stats_spell_id_spell"), "spell_stats", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_spell_stats_spell_id_spell", "spell_stats", "spell", ["spell_id"], ["uuid"]
    )
    op.drop_constraint(
        op.f("fk_spell_effect_spell_stat_id_spell_stats"),
        "spell_effect",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_spell_effect_spell_stat_id_spell_stats",
        "spell_effect",
        "spell_stats",
        ["spell_stat_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_spell_spell_variant_pair_id_spell_variant_pair"),
        "spell",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_spell_spell_variant_pair_id_spell_variant_pair",
        "spell",
        "spell_variant_pair",
        ["spell_variant_pair_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_set_translation_set_id_set"), "set_translation", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_set_translation_set_id_set", "set_translation", "set", ["set_id"], ["uuid"]
    )
    op.drop_constraint(
        op.f("fk_item_type_slot_item_slot_id_item_slot"),
        "item_type_slot",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_item_type_slot_item_type_id_item_type"),
        "item_type_slot",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_item_type_slot_item_type_id_item_type",
        "item_type_slot",
        "item_type",
        ["item_type_id"],
        ["uuid"],
    )
    op.create_foreign_key(
        "fk_item_type_slot_item_slot_id_item_slot",
        "item_type_slot",
        "item_slot",
        ["item_slot_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_item_translation_item_id_item"), "item_translation", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_item_translation_item_id_item",
        "item_translation",
        "item",
        ["item_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_item_stat_translation_item_stat_id_item_stat"),
        "item_stat_translation",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_item_stat_translation_item_stat_id_item_stat",
        "item_stat_translation",
        "item_stat",
        ["item_stat_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_item_item_type_id_item_type"), "item", type_="foreignkey"
    )
    op.drop_constraint(op.f("fk_item_set_id_set"), "item", type_="foreignkey")
    op.create_foreign_key("fk_item_set_id_set", "item", "set", ["set_id"], ["uuid"])
    op.create_foreign_key(
        "fk_item_item_type_id_item_type",
        "item",
        "item_type",
        ["item_type_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_equipped_item_exo_equipped_item_id_equipped_item"),
        "equipped_item_exo",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_equipped_item_exo_equipped_item_id_equipped_item",
        "equipped_item_exo",
        "equipped_item",
        ["equipped_item_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_equipped_item_item_id_item"), "equipped_item", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_equipped_item_custom_set_id_custom_set"),
        "equipped_item",
        type_="foreignkey",
    )
    op.drop_constraint(
        op.f("fk_equipped_item_item_slot_id_item_slot"),
        "equipped_item",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_equipped_item_item_slot_id_item_slot",
        "equipped_item",
        "item_slot",
        ["item_slot_id"],
        ["uuid"],
    )
    op.create_foreign_key(
        "fk_equipped_item_item_id_item", "equipped_item", "item", ["item_id"], ["uuid"]
    )
    op.create_foreign_key(
        "fk_equipped_item_custom_set_id_custom_set",
        "equipped_item",
        "custom_set",
        ["custom_set_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_custom_set_stat_custom_set_id_custom_set"),
        "custom_set_stat",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_custom_set_stats_custom_set_id_custom_set",
        "custom_set_stat",
        "custom_set",
        ["custom_set_id"],
        ["uuid"],
    )
    op.drop_constraint(
        op.f("fk_class_translation_class_id_class"),
        "class_translation",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_class_translation_class_id_class",
        "class_translation",
        "class",
        ["class_id"],
        ["uuid"],
    )
    # ### end Alembic commands ###
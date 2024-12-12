from odoo import api, fields, models, _


class Attendee(models.Model):
    _name = "academic.attendee"
    _rec_name = "name"
    name = fields.Char("Name")
    session_id = fields.Many2one(
        comodel_name="academic.session",
        string="Session",
        required=False,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=False,
    )

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        # manggil function
        self.name = self.partner_id.id

    _sql_constraints = [
        (
            "partner_session_unique",
            "UNIQUE(partner_id,session_id)",
            "You cannot insert the same attendee multiple times!",
        ),
    ]
    course_id = fields.Many2one(
        comodel_name="academic.course",
        string="Course",
        required=False,
        related="session_id.course_id",
        store=True,
    )

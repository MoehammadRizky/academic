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

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        # manggil function
        self.name = self.partner_id.id

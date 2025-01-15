from odoo import api, fields, models, _


class CreateAttendeeWizard(models.TransientModel):
    _name = "academic.create.attendee.wizard"
    
    session_id = fields.Many2one(
        comodel_name="academic.session",
        string="Session",
    )

    session_ids = fields.Many2many(
        comodel_name="academic.session",
        string="Sessions",
    )

    partner_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Attendees untuk ditambahkan",
        required=True,
    )

    def action_add_attendee(self):
        self.ensure_one()

        for ses in self.session_ids:
            att_data = [{"partner_id": att.id} for att in self.partner_ids]
            ses.attendee_ids = [(0, 0, data) for data in att_data]
        return {"type": "ir.actions.act_window_close"}

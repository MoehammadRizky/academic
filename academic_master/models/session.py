from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import time


class session(models.Model):
    _name = "academic.session"
    name = fields.Char("Name", required=True)
    course_id = fields.Many2one(
        comodel_name="academic.course",
        string="Course",
        required=False,
    )
    instructor_id = fields.Many2one(
        comodel_name="res.partner",
        string="Instructor",
        required=False,
    )
    start_date = fields.Date(
        string="Start Date",
        required=False,
        default=lambda self: time.strftime("%Y-%m-%d"),
    )
    duration = fields.Integer(
        string="Duration",
        required=False,
    )
    seats = fields.Integer(
        string="Seats",
        required=False,
    )
    active = fields.Boolean(string="Active", default=True)

    attendee_ids = fields.One2many(
        comodel_name="academic.attendee",
        inverse_name="session_id",
        string="Attendees",
        required=False,
    )

    taken_seats = fields.Float(
        compute="_calc_taken_seats",
        string="Taken Seat",
        required=False,
    )
    
    image_small = fields.Binary(string="Image Small", )
    
    state = fields.Selection(
        string="State",
        selection=[("draft", "Draft"), ("open", "Open"), ("done", "Done")],
        required=True,
        default='draft',  # Menambahkan default state
        states={
            'done': [('readonly', True)],  # Contoh penggunaan states
        }
    )

    def action_open(self):
        self.state = "open"


    def action_done(self):
        self.state = "done"


    def action_draft(self):
        self.state = "draft"


    @api.depends("attendee_ids", "seats")
    def _calc_taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats
            else:
                rec.taken_seats = 0.0

    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {}, name=_("copied from %s") % self.name)
        return super(session, self).copy(default=default)

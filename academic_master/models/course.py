from odoo import api, fields, models, _


class Course(models.Model):
    _name = "academic.course"
    _rec_name = "name"

    name = fields.Char("Name")
    description = fields.Text(
        string="Description",
        required=False,
    )
    responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible")

    session_ids = fields.One2many(
        comodel_name="academic.session",
        inverse_name="course_id",
        string="Sessions",
        required=False,
        ondelete="cascade",
    )

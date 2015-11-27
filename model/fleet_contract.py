from openerp import models, fields

class FleetContractWithAttachment(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    
    attachments_ids = fields.Many2many('ir.attachment', string="Attachments")
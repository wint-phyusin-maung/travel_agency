from odoo import api, fields, models 
from odoo.exceptions import UserError 

class TravelDriverHistory(models.Model):
    _name = 'travel.driver.history'
    _description = 'TravelDriverHistory'
    _rec_name = 'car_driver'

    travel_car_id  = fields.Many2one('travel.car')
    travel_agency = fields.Many2one('travel.agency',related='travel_car_id.travel_agency_id',string="Travel Agency")
    car_driver = fields.Many2one('res.partner')
    join_date = fields.Date()
    fired_date = fields.Date()


    @api.constrains('join_date','fired_date')
    def check_join_date_be_greater(self):
        if self.fired_date > self.join_date:
            raise UserError('Join date must be greater than fired date.')





    

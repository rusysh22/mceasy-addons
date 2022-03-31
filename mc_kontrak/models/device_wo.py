from odoo import models, fields, api, _

class DeviceWO(models.Model):
    _name = 'mc_kontrak.device_wo'
    _description = 'Modul yang berisi pemasangan dari WO dan berelasi ke Contact'

    x_jenis_kendaraan = fields.Many2one('mc_kontrak.jenis_kendaraan', string="Jenis Kendaraan")
    x_nopol = fields.Char(string='Nopol')
    x_tahun = fields.Char(string='Tahun')
    x_imei = fields.Char(string='IMEI')
    x_simcard = fields.Char(string='No Simcard')
    x_tgl_start_pasang = fields.Datetime(string="Tgl Start Pasang")
    x_tgl_end_pasang = fields.Datetime(string="Tgl End Pasang")

    # Relasi
    x_work_order_id = fields.Many2one('mc_kontrak.work_order', ondelete='cascade')
    x_partner_id = fields.Many2one('res.partner')

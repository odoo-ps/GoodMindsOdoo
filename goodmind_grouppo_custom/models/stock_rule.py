from odoo import api, fields, models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    # Inherited methods
    def _make_po_get_domain(self, company_id, values, partner):
        """
            To remove the domain which does not considers lead time or different dates.
            To make it work like v13.
        """
        if values.get('orderpoint_id'):
            del values['orderpoint_id']
        return super(StockRule, self)._make_po_get_domain(company_id=company_id, values=values, partner=partner)

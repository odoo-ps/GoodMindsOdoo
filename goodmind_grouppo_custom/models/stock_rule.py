from odoo import api, fields, models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    # Inherited methods
    def _make_po_get_domain(self, company_id, values, partner):
        """
            To remove the domain which does not consider lead time or different dates.
            To make it work like v13.
        """
        if 'orderpoint_id' in values.keys():
            storing_order_point_temporary = values.get('orderpoint_id')
            del values['orderpoint_id']
            without_order_point = super(StockRule, self)._make_po_get_domain(company_id=company_id, values=values,
                                                                             partner=partner)
            values.update({'orderpoint_id': storing_order_point_temporary})
            return without_order_point
        else:
            return super(StockRule, self)._make_po_get_domain(company_id, values, partner)

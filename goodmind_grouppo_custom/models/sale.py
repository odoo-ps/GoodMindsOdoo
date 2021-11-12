from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Inherited methods
    def _prepare_invoice(self):
        """
            Inherited to make the addition of the terms and conditions by back order details.
            :return: res with the narration field update by custom logic
        """
        res = super(SaleOrder, self)._prepare_invoice()
        back_order_products_data = ""
        back_ordered_deliveries = self.picking_ids.filtered(
            lambda picking: picking.backorder_id != False and picking.state not in ['done', 'cancel'])
        for move in back_ordered_deliveries.move_ids_without_package:
            back_order_products_data = back_order_products_data + "-" + move.product_id.name + ": " + str(
                move.product_uom_qty) + " " + move.product_uom.name + "\n"
        if back_order_products_data:
            res['narration'] = "Backordered Items:\n" + back_order_products_data
        return res

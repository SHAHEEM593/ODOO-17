/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";


patch(Order.prototype, {
     pay() {
     if(this.pos.config.pos_check){
    var category = this.pos.config.pos_category_limit_cat_ids
    var amount = this.pos.config.pos_category_limit_amt
    var discount  = this.pos.config.pos_category_limit_disc
    var order = this.get_orderlines()
    var order_discount = 0
    var order_price = 0

    for (let orders of order){
        var OrderCategory = orders.product.pos_categ_ids
            for (let order_cat of OrderCategory ){
                for (let categs of category){
                    if (categs == order_cat){
                        order_discount += orders.discount
                        order_price += orders.price
                }
                }
                }
                }

    const discounted_amount = (order_discount/100) * order_price
    var error = 0
    if(this.pos.config.pos_discount == 'amount'){
        if ((amount > 1) && (discounted_amount > amount)){
        error += 1
      this.env.services.popup.add(ErrorPopup, {
        title: _t("Error"),
        body: _t('Discount Amount Exceeds'),
     });
    }
    }
    if(this.pos.config.pos_discount == 'percentage'){
    if ((discount > 1) && (order_discount > discount)){
             error += 1
          this.env.services.popup.add(ErrorPopup, {
        title: _t("Error"),
        body: _t('Discount  Exceeds'),
     });}
    }
    if (error == 0 ){
       return{ ...super.pay(),}
    }
    }

    }

});
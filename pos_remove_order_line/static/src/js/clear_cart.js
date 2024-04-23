/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Order } from "@point_of_sale/app/store/models";


patch(ProductScreen.prototype, {
    clearAllCart(){
    console.log(this)
    var order = this.pos.get_order().orderlines;
    console.log(order)
    while (order.length > 0){
            this.pos.get_order().removeOrderline(order[0])
    }
    }

});
/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Order } from "@point_of_sale/app/store/models";


patch(Orderline.prototype, {
    setup(){
    this.pos = usePos()
    },
    async clearSelectedCart(){
    console.log(this)
        var product  = this.props.line.productName
        var order = this.pos.get_order().orderlines
        for(let i in order){
        if(order[i].full_product_name == product){
                  this.pos.get_order().removeOrderline(order[i])

        }
        }
    }
});
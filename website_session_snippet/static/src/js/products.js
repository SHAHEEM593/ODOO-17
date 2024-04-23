/** @odoo-module */

import PublicWidget from '@web/legacy/js/public/public_widget';
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

PublicWidget.registry.Products =  PublicWidget.Widget.extend({
    selector='.prod_snip'
    start: function(){
        jsonrpc('/product_snippets').then((res)=>{
        if (res){
                this.$el.find('#prod_snippets').html(renderToElement('website_session_snippet.product_temp',{res:res}))
        }
        });
        return this._super.apply(this,arguments)
    }
});
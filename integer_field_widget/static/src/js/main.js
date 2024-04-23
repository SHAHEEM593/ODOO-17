/** @odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { useInputField } from "@web/views/fields/input_field_hook";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { useRef,useState,Component } from "@odoo/owl";


export class FloatWidgetNew extends Component {
    static template = "FieldConvert";
    static props = {
        ...standardFieldProps,
        inputType: { type: String, optional: true },
    };
    setup() {
        super.setup();
        this.input = useRef('convert_to_inte');
        useInputField({ getValue: () => this.floatToInt(this.props.record.data[this.props.name]), refName: "convert_to_inte" });
    }
    floatToInt(value) {
        return Math.round(parseFloat(value));
    }
}
export const floatWidgetNew = {
    component: FloatWidgetNew,
    displayName: _t("FieldConvert"),
    supportedTypes: ["float"],
};

registry.category("fields").add("float_to_int_widget", floatWidgetNew);

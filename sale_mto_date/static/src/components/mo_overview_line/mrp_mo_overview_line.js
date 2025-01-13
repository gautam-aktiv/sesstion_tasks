/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { MoOverviewLine } from "@mrp/components/mo_overview_line/mrp_mo_overview_line";

patch(MoOverviewLine.prototype, {
    props: {
        ...MoOverviewLine.props,
        data: {
            ...MoOverviewLine.props.data,
            shape: {
                ...MoOverviewLine.props.data.shape,
                mto_date: String,
            },
        },
    },
    setup() {
        super.setup();
    }
});

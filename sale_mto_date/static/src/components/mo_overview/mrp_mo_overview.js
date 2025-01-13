/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { MoOverview } from "@mrp/components/mo_overview/mrp_mo_overview";

patch(MoOverview.prototype, {
    async getManufacturingData() {
        await super.getManufacturingData();
        this.state.data.summary["mto_date"] = this.state.data.mto_date;
    },
});

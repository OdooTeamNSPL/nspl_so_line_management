/** @odoo-module **/

import { ListRenderer } from "@web/views/list/list_renderer";
import { patch } from "@web/core/utils/patch";

patch(ListRenderer.prototype, {

    /**
     * Handle add line button click
     */
    async _onAddLineButtonClick(ev) {
        ev.preventDefault();
        ev.stopPropagation();

        const button = ev.currentTarget;
        const row = button.closest('tr');

        if (!row) return;

        // Get record ID from the row
        const recordElement = row.querySelector('[data-id]');
        if (!recordElement) return;

        const recordId = parseInt(recordElement.dataset.id);
        if (!recordId) return;

        try {
            // Call the backend method
            await this.env.services.orm.call(
                'sale.order.line',
                'add_line_after',
                [recordId]
            );

            // Reload the view
            await this.props.list.model.root.load();
            this.render(true);

        } catch (error) {
            console.error("Error adding new line:", error);
            this.env.services.notification.add(
                "Error adding new line. Please try again.",
                { type: 'danger' }
            );
        }
    },

    /**
     * Setup event listeners
     */
    setup() {
        super.setup();

        // Bind the click handler
        this._onAddLineButtonClick = this._onAddLineButtonClick.bind(this);
    },

    /**
     * Add event listeners after render
     */
    onMounted() {
        super.onMounted();
        this._addEventListeners();
    },

    onPatched() {
        super.onPatched();
        this._addEventListeners();
    },

    /**
     * Add event listeners to buttons
     */
    _addEventListeners() {
        const buttons = this.el?.querySelectorAll('.oe_add_line_button, .oe_add_line_button_alt');
        if (buttons) {
            buttons.forEach(button => {
                button.removeEventListener('click', this._onAddLineButtonClick);
                button.addEventListener('click', this._onAddLineButtonClick);
            });
        }
    }
});
function select_all_rows(level, fragment) {  // Select all records on the page
    const container = document.querySelector('[id="' + level.toString() + '_' + fragment + '"]');
    const all_selectable_records = container.querySelectorAll('[class~="' + level.toString() + '_select_record"]');
    const selector_all_rows = container.querySelector('[id="' + level.toString() + '_' + fragment + '_id_select_all_rows"]')
    const remove_text = level.toString() + '_' + fragment + '_id_select_record'
    for (let i = 0, n = all_selectable_records.length; i < n; i++) {
        all_selectable_records[i].checked = selector_all_rows.checked
        if (selector_all_rows.checked) {
            $('#' + level.toString() + '_' + fragment + ' #' + all_selectable_records[i].id.replace("id_select_record", "tr")).addClass('recordselectedforaction');
            add_selected_record_to_temp_list(level, fragment, all_selectable_records[i].id.replace(remove_text, ''))
        } else {
            $('#' + level.toString() + '_' + fragment + ' #' + all_selectable_records[i].id.replace("id_select_record", "tr")).removeClass('recordselectedforaction');
            remove_selected_record_from_temp_list(level, fragment, all_selectable_records[i].id.replace(remove_text, ''))
        }
    }
}

function select_or_deselect_a_row(level, fragment, lngid = 0) {  // Select or unselect a row
    const container = document.querySelector('[id="' + level.toString() + '_' + fragment + '"]');
    const selected_record = container.querySelector('[id="' + level.toString() + '_' + fragment + '_id_select_record' + lngid.toString() + '"]');
    const selected_row = container.querySelector('[id="' + level.toString() + '_' + fragment + '_tr' + lngid.toString() + '"]');
    if (lngid > 0) {
        if (selected_record.checked) {
            selected_row.classList.add('recordselectedforaction');
            add_selected_record_to_temp_list(level, fragment, lngid);
        } else {
            selected_row.classList.remove('recordselectedforaction');
            remove_selected_record_from_temp_list(level, fragment, lngid);
        }
    }
}

function check_if_check_is_checked(level, fragment, lngid) {
    const container = document.querySelector('[id="' + level.toString() + '_' + fragment + '"]');
    const selected_record = container.querySelector('[id="' + level.toString() + '_' + fragment + '_id_select_record' + lngid.toString() + '"]');
    selected_record.checked = !selected_record.checked;
    select_or_deselect_a_row(level, fragment, lngid)
}

function add_selected_record_to_temp_list(level, fragment, lngid) {
    const container = document.querySelector('[id="' + level.toString() + '_' + fragment + '"]');
    var templistid = level.toString() + "_" + fragment + "_multiselect_records"
    var templist = container.querySelector('[id="' + templistid + '"]');
    if (!templist) {
        var create_fragment = document.createElement("input");
        create_fragment.type = "hidden";
        create_fragment.id = templistid;
        // create_fragment.value = ""
        $("#" + level.toString() + "_" + fragment).prepend(create_fragment);  // Create a non existing fragment templist
        templist = container.querySelector('[id="' + templistid + '"]')  // Necessary to bind the new created fragment to the variable
    }
    var templist_items = []  // define a list
    if (templist.value) {
        templist_items = templist.value.split(',')  // Put the value from the templist in the list items
    }
    if (jQuery.inArray(lngid, templist_items) > -1) {
    } else {
        templist_items.push(lngid)  // Add the lngid to the list
    }
    templist.value = templist_items  // Set the list to the templist
    set_number_selected_rows(level, fragment)
}

function remove_selected_record_from_temp_list(level, fragment, lngid) {
    const container = document.querySelector('[id="' + level.toString() + '_' + fragment + '"]');
    var templistid = level.toString() + "_" + fragment + "_multiselect_records";
    var templist = container.querySelector('[id="' + templistid + '"]');
    var templist_items = [];  // define a list
    if (templist.value) {
        templist_items = templist.value.split(',');  // Put the value from the templist in the templist items
    }
    var not_delete_list = []
    for (num = 0, til = templist_items.length; num < til; num++) {
        if (templist_items[num] !== lngid.toString()) {
            not_delete_list.push(templist_items[num]);
        }
    }
    templist.value = not_delete_list;  // Set the list to the templist
    set_number_selected_rows(level, fragment)
}

function set_number_selected_rows(level, fragment) {   // set number selected rows and disable the action button if necessary
    const container = document.querySelector('[id="' + level.toString() + '_' + fragment + '"]');
    const actionbutton = container.querySelector('[id="' + level.toString() + '_' + fragment + '_process_selected_records"]')
    const deletebutton = container.querySelector('[id="' + level.toString() + '_' + fragment + '_delete_selected_records"]')
    const id_number_selected_rows = container.querySelector('[id="' + level.toString() + '_' + fragment + '_id_number_selected_rows"]');
    var number = 0
    const multiselect_records = container.querySelector('[id="' + level.toString() + '_' + fragment + '_multiselect_records"]');
    if (multiselect_records) {
        if (multiselect_records.value) {
            var templist_items = multiselect_records.value.split(',');  // Put the value from the templist in the templist items
            number = templist_items.length
        }
    }
    if (number > 0) {
        id_number_selected_rows.innerHTML = number.toString() + " geselecteerd"
        actionbutton.disabled = false
        if (deletebutton) {
            deletebutton.disabled = false
        }
    } else {
        id_number_selected_rows.innerHTML = ""
        actionbutton.disabled = true
        if (deletebutton) {
            deletebutton.disabled = true
        }
    }
}

function check_row_selection(level, fragment) {
    const container = document.querySelector('[id="' + level.toString() + '_' + fragment + '"]');
    var enable_button = false
    const selector_all_rows = container.querySelector('[id="' + level.toString() + '_' + fragment + '_id_select_all_rows"]');
    if (selector_all_rows) {
        if (selector_all_rows.checked) {
            selector_all_rows.checked = false;
        }
    }
    const multiselect_records = container.querySelector('[id="' + level.toString() + '_' + fragment + '_multiselect_records"]');
    if (multiselect_records) {
        if (multiselect_records.value) {
            var templist_items = multiselect_records.value.split(',');  // Put the value from the templist in the templist items
            for (var num = 0, til = templist_items.length; num < til; num++) {
                var selected_row = container.querySelector('[id="' + level.toString() + '_' + fragment + '_tr' + templist_items[num].toString() + '"]')
                selected_row.classList.add('recordselectedforaction')
                if (selected_row) {
                    container.querySelector('[id="' + level.toString() + '_' + fragment + '_id_select_record' + templist_items[num].toString() + '"]').checked = true
                    enable_button = true
                }
            }
        }
    }
    if (enable_button) {
        const actionbutton = container.querySelector('[id="' + level.toString() + '_' + fragment + '_process_selected_records"]')
        if (actionbutton) {
            actionbutton.disabled = false
        }
        const deletebutton = container.querySelector('[id="' + level.toString() + '_' + fragment + '_delete_selected_records"]')
        if (deletebutton) {
            deletebutton.disabled = false
        }
    }
}

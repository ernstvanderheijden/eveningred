var i = 0;
var n = 0;

function do_url_href(fragment, level, url) {
    if (!url.includes('&multiselect_records')) {
        url = url + "&multiselect_records="
        if ($('#' + (level - 1).toString() + '_' + fragment + '_multiselect_records').length > 0) {
            url = url + document.getElementById((level - 1).toString() + '_' + fragment + '_multiselect_records').value
        }
    }
    window.open(url, "_parent")
}

function do_url(fragment, level, url) {
    if (!fragment) {
        fragment = 'chapter'
        if (level > 0) {
            fragment = level.toString() + '_modal'
        }
    }
    if (!url.includes('&multiselect_records')) {
        url = url + "&multiselect_records="
        if ($('#' + (level - 1).toString() + '_' + fragment + '_multiselect_records').length > 0) {
            url = url + document.getElementById((level - 1).toString() + '_' + fragment + '_multiselect_records').value
        }
    }
    if (!url.includes('&filter')) {
        if ($('[id="' + level.toString() + '_' + fragment + '"] .filterfield').length > 0) {
            //Add filter to url
            url = add_filter_to_url(fragment, level, url);
        }
    }
    // Execute a given url with ajax
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        async: true,
        headers: {'X-Requested-With': 'XMLHttpRequest'},
        data: {},
        success: function (data) {
            var load_template = get_load_template(data)
            if (load_template && data.form_is_valid) {
                window.open(data.successurl, '_parent');
            } else if (data.form_is_valid) {
                var targetfragment = data.fragment
                if (data.level > 0) {
                    targetfragment = 'body'
                }
                if (data.html_header && data.level > 0) {
                    document.getElementById(data.level.toString() + "_header").innerHTML = data.html_header;
                }
                if (data.html_body) {
                    document.getElementById(data.level.toString() + "_" + targetfragment).innerHTML = data.html_body;
                }
                if (data.html_footer && data.level > 0) {
                    document.getElementById(data.level.toString() + "_footer").innerHTML = data.html_footer;
                }
                if (data.level > 0) {
                    set_classes_jqdialog(data) // Herewith we set the classes for the modal.dialog div
                    var modallevel = $("#" + data.level.toString() + "_modal")
                    if (modallevel.length > 0) {
                        modallevel.modal('show');
                    }
                } else {
                    if (!data.donotclose) {
                        var modal1 = $('#1_modal')
                        if (modal1.is(":visible")) {
                            modal1.modal('hide');
                            $('#1_body').innerHTML = ''
                        }
                    }
                }
                if (data.messagelist) {
                    if (data.messagelist[2]) {
                        handle_messagelist(data.messagelist)
                    }
                }
                if (data.clickevent === 'selectmultiple') {
                    check_row_selection(data.level, data.fragment)  // Check if rows must be selected
                }
            } else {
                handle_messagelist(data.messagelist)
            }
            if ($(".js-save-form").length > 0) {
                var id_binded_form = $("#" + level.toString() + "_id_binded_form");
                if (id_binded_form.val() === "False") {
                    var form = $("#" + level.toString() + "_modal");
                    form.on("submit", ".js-save-form", {'level': level}, save_form);
                    id_binded_form.val("True");
                }
                /* Passing data to a function ('save_form') in jquery is done by {'key':'value'} ('{'level': level}') and
                   then by calling function_variable_name.data.key in the function where this is used (see 'save_form(event)' 'event.data.level') */
            }
            if (data.print_records && data.print_type && data.form_is_valid) {
                open_records_in_new_tab(data.print_records, data.print_type);
            }
        }
    });
    return false;
}

function refresh_content(fragment, level, url) {
    if (!url.includes('&filter')) {
        //Add filter to url
        url = add_filter_to_url(fragment, level, url);
    }
    // Execute a given url with ajax
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        async: true,
        headers: {'X-Requested-With': 'XMLHttpRequest'},
        data: {},
        success: function (data) {
            if (data.form_is_valid) {
                if (data.fragmentrefresh && data.html_body) {
                    document.getElementById(data.level.toString() + "_" + data.fragmentrefresh).innerHTML = data.html_body;
                }
                if (data.refreshtarget === 'data' && data.html_pagination) {
                    document.getElementById(data.level.toString() + "_pagination_" + data.fragment).innerHTML = data.html_pagination;
                }

            } else {
                handle_messagelist(data.messagelist)
            }
        }
    });
    return false;
}

function show_ctx(level, url, ctxdata) {
    // Execute a given url with ajax
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        async: true,
        headers: {'X-Requested-With': 'XMLHttpRequest'},
        data: {'ctxdata': ctxdata},
        proccessData: false, // to prevent the data being added to the url ==> for large amounts of data
        contentType: false,
        cache: false,
        success: function (data) {
            if (data.form_is_valid) {
                if (data.html_header && data.level > 0) {
                    document.getElementById(data.level.toString() + "_header").innerHTML = data.html_header;
                }
                document.getElementById(data.level.toString() + "_" + data.fragment).innerHTML = data.html_body;
                if (data.html_footer && data.level > 0) {
                    document.getElementById(data.level.toString() + "_footer").innerHTML = data.html_footer;
                }
                set_classes_jqdialog(data) // Herewith we set the classes for the modal.dialog div
                var modallevel = $("#" + data.level.toString() + "_modal")
                if (modallevel.length > 0) {
                    modallevel.modal('show');
                }
            } else {
                handle_messagelist(data.messagelist)
            }
        }
    });
    return false;
}

function save_form(event) {

    // CRUD handling for modals via Ajax
    // Set buttons in the footer disabled
    $("button", "#" + event.data.level.toString() + "_footer").attr("disabled", "disabled");

    var form = $("#form" + event.data.level.toString())
    /* Passing data to a function ('save_form') in jquery is done by {'key':'value'} ('{'level': level}') and
       then by calling function_variable_name.data.key in the function where this is used (see 'save_form(event)' 'event.data.level') */

    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        async: true,
        headers: {'X-Requested-With': 'XMLHttpRequest'},
        dataType: 'json',
        success: function (data) {
            if (data.form_is_valid) {
                if (data.messagelist) {
                    if (data.messagelist[3]) {
                        handle_messagelist(data.messagelist)
                    }
                }
                if (data.closelevel) {  // On delete from a modal, the modal itself must be hidden
                    $("#" + data.closelevel.toString() + "_modal").modal('hide')
                    remove_classes_jqdialog(data.closelevel)
                }
                crud_return_handler(data);
            } else {
                form.replaceWith(data['html_body']);
            }
            $("button", "#" + event.data.level.toString() + "_footer").attr("disabled", false);
            if (data.print_records && data.print_type && data.form_is_valid) {
                open_records_in_new_tab(data.print_records, data.print_type);
            }
        }
    })
    return false;
}

function save_value(valuefield_id, level, namepackage, namefragment, namefield, recordid, refresh_fragment = false, refresh_level = 0, refresh_target = '', fk = '') {
    var valuefield = document.getElementById(valuefield_id);
    var strvalue = valuefield.value;
    var dataurl = "/shared/save_value/?level=" + level + "&package=" + namepackage + "&fragment=" + namefragment + "&pk=" + recordid.toString() + "&namefield=" + namefield;
    var editfield = '';
    $.ajax({
        url: dataurl,
        type: 'post',
        dataType: 'json',
        data: {'key': strvalue},
        success: function (data) {
            if (data.form_is_valid) {
                valuefield.classList.remove("is-invalid")
                if (data.refresh_fields) {
                    for (const [key, value] of Object.entries(data.refresh_fields)) {
                        if (key === 'fragment') {
                            for (const [fragment_key, fragment_value] of Object.entries(value)) {
                                document.getElementById(fragment_key).innerHTML = fragment_value;
                            }
                        } else {
                            editfield = $('#' + level.toString() + '_edit_' + key + "_" + data.recordid.toString());
                            if (editfield.length > 0) {  // check for inputfield
                                editfield.attr("value", value.replace(".", ","));
                                editfield.val(value.replace(".", ","))
                            }
                        }
                    }
                }
                handle_messagelist(data.messagelist)
            } else {
                valuefield.classList.add("is-invalid")
                handle_messagelist(data.messagelist)
            }
            if (refresh_fragment) {
                do_refresh_fragment("", refresh_target, refresh_level, "/core/fragment/?level=0&package=" + namepackage + "&fragment=" + refresh_target + "&pk=" + fk + "&fk=&refreshtarget=data&fragmentrefresh=data_" + refresh_target + "&successurl=&page=1&paginate=1")
            }
        }
    });
    return false;
}

function save_checkbox(checkedfield_id, level, namepackage, namefragment, namefield, recordid, refresh_fragment = false, refresh_level = 0, refresh_target = '', fk = '') {
    var is_checked = document.getElementById(checkedfield_id).checked;
    var dataurl = "/shared/save_checkbox/?level=" + level + "&package=" + namepackage + "&fragment=" + namefragment + "&pk=" + recordid.toString() + "&namefield=" + namefield;
    $.ajax({
        url: dataurl,
        type: 'post',
        dataType: 'json',
        data: {'key': is_checked},
        success: function (data) {
            handle_messagelist(data.messagelist)
        }
    });
    return false;
}

function save_record(level, namepackage, namefragment, strid, pk, fk, valuelist, id_button, refresh_fragment = false, refresh_level = 0, refresh_target = '', successurl = '') {
    var val_key = ''
    var val_value = 0
    var values = valuelist.split(',')
    var dict_fields_and_values = []
    for (i = 0; i < values.length; i++) {  // create a dict
        val_key = level.toString() + '_edit_' + values[i] + '_' + strid.toString()
        if ($('#' + level.toString() + '_edit_' + values[i] + '_' + strid.toString()).length) {
            if (document.getElementById(level.toString() + '_edit_' + values[i] + '_' + strid.toString()).value) {
                val_value = document.getElementById(level.toString() + '_edit_' + values[i] + '_' + strid.toString()).value
            } else {
                val_value = ""
            }
            dict_fields_and_values.push({key: val_key, value: val_value})
        }
    }
    var dataurl = "/shared/save_record/?level=" + level + "&package=" + namepackage + "&fragment=" + namefragment + "&recordid=" + strid.toString() + "&pk=" + pk.toString() + "&fk=" + fk.toString() + "&successurl=" + successurl;
    $.ajax({
        url: dataurl,
        //traditional: true,
        type: 'post',
        dataType: 'json',
        data: {'dict_fields_and_values': JSON.stringify(dict_fields_and_values)},
        success: function (data) {
            if (data.form_is_valid) {
                if ((level.toString() + "_usage_electricity_" + strid).length > 0) {
                    $('#' + level.toString() + "_usage_electricity_" + strid).text(data.usage_electricity);
                    $('#' + level.toString() + "_previous_recordingdate_electricity_" + strid).text(data.previous_recordingdate_electricity);
                    $('#' + level.toString() + "_previous_electricity_" + strid).text(data.previous_electricity);
                    set_warning_class_utilityusage(level, 'electricity', data.warning_electricity, strid)
                    $("#" + level.toString() + "_span_previous_electricity_" + strid).css("display", "block");
                    $('#' + level.toString() + "_usage_gas_" + strid).text(data.usage_gas);
                    $('#' + level.toString() + "_previous_recordingdate_gas_" + strid).text(data.previous_recordingdate_gas);
                    $('#' + level.toString() + "_previous_gas_" + strid).text(data.previous_gas);
                    set_warning_class_utilityusage(level, 'gas', data.warning_gas, strid)
                    $("#" + level.toString() + "_span_previous_gas_" + strid).css("display", "block");
                    $('#' + level.toString() + "_usage_water_" + strid).text(data.usage_water);
                    $('#' + level.toString() + "_previous_recordingdate_water_" + strid).text(data.previous_recordingdate_water);
                    $('#' + level.toString() + "_previous_water_" + strid).text(data.previous_water);
                    set_warning_class_utilityusage(level, 'water', data.warning_water, strid)
                    $("#" + level.toString() + "_span_previous_water_" + strid).css("display", "block");
                }
                handle_messagelist(data.messagelist)
                $('#' + id_button).prop("disabled", true);
                document.getElementById(id_button).style.visibility = "hidden"
                if ($('#' + id_button + "_check").length) {
                    document.getElementById(id_button + "_check").style.visibility = ""
                }
                if (data.refresh_fields) {
                    for (const [key, value] of Object.entries(data.refresh_fields)) {
                        if (key === 'fragment') {
                            for (const [fragment_key, fragment_value] of Object.entries(value)) {
                                $('#' + fragment_key).html(fragment_value);
                            }
                        }
                    }
                }
            } else {
                handle_messagelist(data.messagelist)
            }
            if (data.successurl) {
                if (data.successurl.includes('/core/template/')) {
                    window.open(data.successurl, '_parent')
                }
            }
            if (data.print_records && data.print_type && data.form_is_valid) {
                open_records_in_new_tab(data.print_records, data.print_type);
            }
        }
    });
    return false;
}

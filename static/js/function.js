var i = 0;
var n = 0;
var num = 0;
var til = 0;

function keyinputOk(key) {
    return key !== "Meta" && key !== "Escape" && key !== "Alt" && key !== "Tab" && key !== "Control" && key !== "Shift" && key !== "CapsLock" && key !== "Enter" && key !== "ArrowUp" && key !== "ArrowRight" && key !== "ArrowDown" && key !== "ArrowLeft";
}

function redirect_no_rights(data) {
    if (data.not_allowed) {
        window.open("/403/", "_parent");
        return true
    }
}

function set_element_disabled(id) {
    document.getElementById(id).disabled = true;
}

function disable_element_onclick(id) {
    document.getElementById(id).onclick = "";
}

function set_active_level(level) {
    document.getElementById('activelevel').value = level
}

function get_load_template(data) {
    var load_template = false
    if (data.successurl) {
        if (data.successurl.includes('/core/template/')) {
            load_template = true
        } else if (data.successurl.includes('/public/contract/')) {
            load_template = true
        } else if (data.successurl.includes('/public/invoice/')) {
            load_template = true
        }
    }
    return load_template
}

function do_refresh_fragment(current_sort_field, fragment, level, url) {
    if (!fragment) {
        fragment = getQueryString(url, 'fragment')
    }
    add_filter_to_url(fragment, level, url)
    set_sort_class(current_sort_field, level)
    refresh_content(fragment, level, url);
}

function crud_return_handler(data) {
    if (data.successurl) {
        if (data.successurl.includes('/core/template/')) {
            window.open(data.successurl, '_parent');
        } else {
            const level = getQueryString(data.successurl, 'level')
            hide_modal(data.level);
            do_refresh_fragment(data.order_by, data.fragment, level, data.successurl)
            remove_classes_jqdialog(data.level)
        }
    }
}

function getQueryString(url, argument) {
    const searchurl = new URL("https://" + url)
    const args = new URLSearchParams(searchurl.search);
    return args.get(argument);
}

function do_refresh_grid(fragment, level, url) {
    // Collect filters
    if ($("#id_estatetype").length > 0) {
        url = url + '&estatetype=' + document.getElementById('id_estatetype').value + '&searchdate=' + document.getElementById('id_searchdate').value
    }
    refresh_content(fragment, level, url);
}

function hide_modal(level) {
    // Function for hiding a modal of a certain level.
    $("#" + level.toString() + "_modal").modal('hide');
    remove_classes_jqdialog(level)
}

function search_ctx() {
    var search_ctx = $(".search_ctx");
    var searchstring = $('#searchfield_ctx').val();
    search_ctx.css("background-color", "#ffffff");
    if (searchstring) {
        $(".search_ctx:contains('" + searchstring + "')").css("background-color", "#ffff00");
    } else {
        search_ctx.css("background-color", "#ffffff");
    }
}

function remove_classes_jqdialog(level) {
    var jqdialog = jQuery("#" + level.toString() + "_dialog");
    jqdialog.removeClass('modal-sm');
    jqdialog.removeClass('modal-md');
    jqdialog.removeClass('modal-lg');
    jqdialog.removeClass('modal-xl');
}

function set_classes_jqdialog(data) {
    //  Function to give size class to div.
    //  Exclude divs with '_inner' in the id.
    //  So the size will not be changed when only the inner part is changed
    if (data.modalsize) {
        var jqdialog = jQuery("#" + data.level.toString() + "_dialog");
        jqdialog.removeClass('modal-sm');
        jqdialog.removeClass('modal-md');
        jqdialog.removeClass('modal-lg');
        jqdialog.removeClass('modal-xl');
        jqdialog.removeClass('modal-fullscreen');
        if (data.modalsize) {
            if (data.modalsize === 'modalsm') {
                jqdialog.addClass('modal-sm');
            } else if (data.modalsize === 'modalmd') {
                jqdialog.addClass('modal-md');
            } else if (data.modalsize === 'modallg') {
                jqdialog.addClass('modal-lg');
            } else if (data.modalsize === 'modalxl') {
                jqdialog.addClass('modal-xl');
            } else if (data.modalsize === 'modalfullscreen') {
                jqdialog.addClass('modal-fullscreen');
            }
        }
    }
}

function set_clicked_value_to_previous_modal(level, field_id_previous_modal, recordid, recordtext) {  // Is used
    // Fill the id and the text of the clicked record in the field from where the select via a searchbutton was started.
    $("#" + (level - 1).toString() + "_modal" + " #id_" + field_id_previous_modal).val(recordid)
    $("#" + (level - 1).toString() + "_modal" + ' #id_modal_select_' + field_id_previous_modal).val(recordtext)
    $("#" + (level - 1).toString() + "_modal" + ' #id_modal_select_div_' + field_id_previous_modal).text(recordtext)
    hide_modal(level);
    remove_classes_jqdialog(level)
}

function save_paginatesize(current_sort_field, fragment, url_save, level, url_get_data) {
    do_url(fragment, level, url_save);
    $(document).ajaxStop(function () {  // Function to wait for the ajax request to be ready and then execute
        do_refresh_fragment(current_sort_field, fragment, level, url_get_data);
        $(this).unbind("ajaxStop");  // Function to stop waiting for ajax requests to be ready
    });
}

var getUrlParameter = function getUrlParameter(dataurl, part_querystring) {  // Function for getting value off the dataurl.querystring
    // Source: https://stackoverflow.com/questions/19491336/how-to-get-url-parameter-using-jquery-or-plain-javascript
    var sPageURL = dataurl.replaceAll("?", "&"),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === part_querystring) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};

function move_columns(strmove, fragment, level, url) {
    var strdate = new Date();
    if (strmove !== 0) {
        strdate = new Date(document.getElementById('id_searchdate').value);
    }
    var time = strdate.getTime(); //convert to milliseconds since epoch
    var newDate = new Date(time + (strmove * 24 * 1000 * 60 * 60));
    var date = new Date(newDate),
        year = date.getFullYear(),
        month = (date.getMonth() + 1).toString(),
        formatedMonth = (month.length === 1) ? ("0" + month) : month,
        day = date.getDate().toString(),
        formatedDay = (day.length === 1) ? ("0" + day) : day;
    document.getElementById('id_searchdate').value = year + "-" + formatedMonth + "-" + formatedDay;
    do_refresh_grid(fragment, level, url)
}

function do_url_with_startdate_and_enddate(fragment, level, url) {
    url = url + "&startdate=" + $("#1_modal #id_startdate").val() + "&enddate=" + $("#1_modal #id_enddate").val()
    do_url(fragment, level, url)
}

function set_estateid_to_null() {  // Is used
    $('#id_estateid')
        .find('option')
        .remove()
        .end()
        .append('<option value="">---</option>')
        .val('');
}

function set_button_enabled(id_button) {
    $('#' + id_button).prop("disabled", false);
    document.getElementById(id_button).style.visibility = ""
    if ($('#' + id_button + "_check").length) {
        document.getElementById(id_button + "_check").style.visibility = "hidden";
    }
}

function do_list_action(fragment, level, url, selections) {
    set_active_level(level)
    // Add action and record id's to the url and with do_url do that action with those records
    var working_level = level
    var list_selected_records = "all"  // If no selections are necessary
    var number_selected_rows = "0"
    if (url.includes('do=true')) {
        working_level = working_level - 1
    }  // Set the level to the uderlaying level, for getting the data from there
    var list_action = $("#" + working_level.toString() + "_id_select_action")
    var list_action_caption = $("#" + working_level.toString() + "_id_select_action" + " option:selected").text()
    if (selections) {  // If selections are necessary
        list_selected_records = $("#" + working_level.toString() + "_" + fragment + "_multiselect_records").val()
        number_selected_rows = $("#" + working_level.toString() + "_id_number_selected_rows").text()
    }

    if ((selections && list_action && number_selected_rows) || selections === false) {
        url = url + '&list_action=' + list_action.val() + '&list_action_caption=' + list_action_caption + '&list_selected_records=' + list_selected_records + '&number_selected_rows=' + number_selected_rows
        do_url(fragment, level, url);
        // If 'do=true' is in the url, the action has been executed and the modal can be hide
        if (url.includes('do=true')) {
            hide_modal(level)
            remove_classes_jqdialog(level)
        }
        list_action.val('')
        // mySelect.setValue('')

    } else {
        list_action.val('')
        // mySelect.setValue('')
    }
}

function do_action(action, fragment, level, url, query_fieldname = '', query_id = '') {
    set_active_level(level)
    // Add action and record id's to the url and with do_url do that action with those records
    if (query_fieldname && query_id) {
        url = url + '&action=' + action + "&" + query_fieldname + "=" + document.getElementById(query_id).value
    } else {
        url = url + '&action=' + action
    }
    do_url(fragment, level, url);
}

function set_warning_class_utilityusage(level, strtype, is_warning, strid) {
    var warning_element = $('#' + level.toString() + "_warning_" + strtype + "_" + strid)
    if (is_warning) {
        warning_element.addClass("badge-danger")
        warning_element.removeClass("badge-success")
    } else {
        warning_element.addClass("badge-success")
        warning_element.removeClass("badge-danger")
    }
}

function save_and_finalize_invoice(level) {
    var formid = $('#form' + (level + 1).toString());
    var straction = formid.attr('action');
    formid.attr('action', straction + "&finalize=true");
    formid.submit();
}

function open_records_in_new_tab(print_records, print_type) {
    // window.open("/shared/action/actions/?level=0&pk=&action=download_" + print_type + "&multiselect_records=" + print_records, "_blank");
    window.location.href = "/shared/action/actions/?level=0&pk=&action=download_" + print_type + "&multiselect_records=" + print_records;
    setInterval(myTimer, 1200);

    function myTimer() {
        location.reload()
    }

}

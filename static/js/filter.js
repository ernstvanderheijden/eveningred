
function set_sort_class(current_sort_field, level) {
    if (current_sort_field) {
        // Set sorting the data by setting the class sorting_desc or asc to the currently clicked sort_field
        var sortfield = $("#" + level.toString() + "_order_by_" + current_sort_field.replace("-",""));
        if (sortfield.hasClass('sorting_desc')) {
            sortfield.removeClass('sorting_desc')
            sortfield.addClass('sorting_asc')
        } else if (sortfield.hasClass('sorting_asc')) {
            sortfield.removeClass('sorting_asc')
            sortfield.addClass('sorting_desc')
        } else {
            $(".sorting_desc").removeClass("sorting_desc").addClass('sorting');
            $(".sorting_asc").removeClass("sorting_asc").addClass('sorting');
            sortfield.addClass('sorting_desc')
        }
    }
}

function do_sort(fragment, current_sort_field, level, url) {
    set_sort_class(current_sort_field, level)
    do_url(fragment, level, url);
}

function add_filter_to_url(fragment, level, url) {
    if (url.includes('/core/create/') || url.includes('/core/update/') || url.includes('/core/delete/')) {  // For CRUD put level 1 down
        level = level - 1
    }
    // Construct the filterstring
    var filterstring = "&filter="
    const filterfields = document.querySelectorAll("[id='" + level.toString() + "_" + fragment + "'] .filterfield");  // In the queryselectorAll the ',' means 'OR' ' ' means 'AND'
    filterfields.forEach((filterfield) => {
        filterstring = filterstring + filterfield.id.replace(level.toString() + "_filterfield_","");
        filterstring = filterstring + "~~";
        filterstring = filterstring + filterfield.getAttribute('data-operator');
        filterstring = filterstring + "~~";
        filterstring = filterstring + filterfield.value + ";";
    });
    filterstring = filterstring + construct_order_by_string(fragment, level)
    return url + filterstring
}

function determine_order_by_variables(fragment, level) {
    // Construct the order_by, find all fragments with class 'sorting_desc' (must be 1 at least, if not try again with 'sorting_asc')
    var field_order_by = ""
    var operator_order_by = ""
    if (level > 0) {
        fragment = 'body'
    }
    try{
        if (document.querySelector('[id="' + level.toString() + '_' + fragment + '"] .sorting_desc').id > '') {
            operator_order_by = "desc"
            field_order_by = document.querySelector('[id="' + level.toString() + '_' + fragment + '"] .sorting_desc').id.replace(level.toString() + "_order_by_","");
        }
    } catch {
        try{
            operator_order_by = "asc"
            field_order_by = document.querySelector('[id="' + level.toString() + '_' + fragment + '"] .sorting_asc').id.replace(level.toString() + "_order_by_","");
        } catch {}
    }
    return [operator_order_by, field_order_by]
}

function construct_order_by_string(fragment, level) {
    var order_by_variables = determine_order_by_variables(fragment, level)
    return "order_by~~" + order_by_variables[0] + "~~" + order_by_variables[1]
}

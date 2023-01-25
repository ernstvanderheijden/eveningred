/* If browser back button was used, flush cache */
(function () {
	window.onpageshow = function(event) {
		if (event.persisted) {
			window.location.reload();
		}
	};
})();

function initialize_custom_datepickers(level) {
    const datepickers = document.querySelectorAll('.custom-datepicker');  // In the queryselectorAll the ',' means 'OR' ' ' means 'AND'
    datepickers.forEach((datepick) => {

        const options = {
            title: 'Selecteer een datum',
            weekdaysNarrow: ['Zo', 'Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za'],
            weekdaysShort: ['Zo', 'Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za'],
            weekdaysFull: ['Zondag', 'Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag'],
            monthsShort: ['Jan', 'Feb', 'Maa', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'],
            monthsFull: ['Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli', 'Augustus', 'September', 'Oktober', 'November', 'December'],
            format: 'dd-mm-yyyy',
            cancelBtnLabel: 'Annuleer selectie',
            cancelBtnText: 'Annuleer',
            clearBtnLabel: 'Wis selectie',
            clearBtnText: 'Wis',
            okBtnLabel: 'Kies selectie',
            okBtnText: 'Opslaan',
            startDay: 1,
            startDate: new Date(),
            inline: true,
        }

        if (datepick.dataset.datepickerstart) {
            var datestart = datepick.dataset.datepickerstart.split('-');
            datestart = new Date(datestart[0], datestart[1] - 1, datestart[2]);
            options['startDate'] = datestart
        }

        if (datepick.dataset.datepickermin) {
            var datemin = datepick.dataset.datepickermin.split('-');
            datemin = new Date(datemin[0], datemin[1] - 1, datemin[2]);
            options['min'] = datemin
        }

        if (datepick.dataset.datepickermax) {
            var datemax = datepick.dataset.datepickermax.split('-');
            datemax = new Date(datemax[0], datemax[1] - 1, datemax[2]);
            options['max'] = datemax
        }

        const myDatepicker = new mdb.Datepicker(datepick, options);
    })

}

function initialize_ajax_datepickers(level) {
    const datepickers = document.querySelectorAll('[id="' + level.toString() + '_content"] .ajax-datepicker');  // In the queryselectorAll the ',' means 'OR' ' ' means 'AND'
    datepickers.forEach((datepick) => {

        const options = {
            title: 'Selecteer een datum',
            weekdaysNarrow: ['Zo', 'Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za'],
            weekdaysShort: ['Zo', 'Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za'],
            weekdaysFull: ['Zondag', 'Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag'],
            monthsShort: ['Jan', 'Feb', 'Maa', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'],
            monthsFull: ['Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli', 'Augustus', 'September', 'Oktober', 'November', 'December'],
            format: 'dd-mm-yyyy',
            cancelBtnLabel: 'Annuleer selectie',
            cancelBtnText: 'Annuleer',
            clearBtnLabel: 'Wis selectie',
            clearBtnText: 'Wis',
            okBtnLabel: 'Kies selectie',
            okBtnText: 'Opslaan',
            startDay: 1,
            startDate: new Date(),
            inline: true,
        }

        if (datepick.dataset.datepickerstart) {
            var datestart = datepick.dataset.datepickerstart.split('-');
            datestart = new Date(datestart[0], datestart[1] - 1, datestart[2]);
            options['startDate'] = datestart
        }

        if (datepick.dataset.datepickermin) {
            var datemin = datepick.dataset.datepickermin.split('-');
            datemin = new Date(datemin[0], datemin[1] - 1, datemin[2]);
            options['min'] = datemin
        }

        if (datepick.dataset.datepickermax) {
            var datemax = datepick.dataset.datepickermax.split('-');
            datemax = new Date(datemax[0], datemax[1] - 1, datemax[2]);
            options['max'] = datemax
        }
        const myDatepicker = new mdb.Datepicker(datepick, options);
    })

}

function initialize_ajax_tinymce() {
    tinymce.remove();  // Otherwise it won't init a second time
    tinymce.init({
        selector: '.tinymce',
        plugins: "advlist, lists, table, searchreplace, image",
        toolbar: "undo redo | bold italic underline | outdent indent | alignleft aligncenter alignright alignjustify alignnone | link image | numlist bullist | advlist | table | searchreplace",
    });
}

// Prevent Bootstrap dialog from blocking focusin (For TinyMCE)
document.addEventListener('focusin', (e) => {
    if (e.target.closest(".tox-tinymce-aux, .moxman-window, .tam-assetmanager-root") !== null) {
        e.stopImmediatePropagation();
    }
});


$(document).ready(function () {
    // Disable autocomplete on all input fields
    $('input').attr('autocomplete', 'off');

    initialize_custom_datepickers(0) //work in progress

    // messages timeout for 3 sec
    setTimeout(function () {
        $('.messages').fadeOut('slow');
    }, 3000); // <-- time in milliseconds, 1000 =  1 sec

    // add drag attribute to all modals
    $(".draggable").draggable({
        handle: ".modal-header",
        containment: ".modal",
    });

    // main sidenav
    const sidenav = document.getElementById('sidenav-1');
    const sidenavInstance = mdb.Sidenav.getInstance(sidenav);

    let innerWidth = null;

    const setMode = (e) => {
        // Check necessary for Android devices
        if (window.innerWidth === innerWidth) {
            return;
        }

        innerWidth = window.innerWidth;

        if (sidenavInstance) {
            if (window.innerWidth < 1400) {
                sidenavInstance.changeMode('over');
                sidenavInstance.hide();
            } else {
                sidenavInstance.changeMode('side');
                sidenavInstance.show();
            }
        }
    };

    setMode();

    // Event listeners
    window.addEventListener('resize', setMode);
})


$(document).ajaxComplete(function () {
    // POPOVER
    var level = document.getElementById('activelevel').value;
    // To initialize the popover function after aa ajax call
    const popoversEl = document.querySelectorAll('[id="' + level.toString() + '_content"] [data-mdb-toggle="popover"]', '[id="' + level.toString() + '_modal"] [data-mdb-toggle="popover"]');  // In the queryselectorAll the ',' means 'OR' ' ' means 'AND'
    popoversEl.forEach((popoverEl) => {
        const popover = new mdb.Popover(popoverEl);
    })

    // Disable autocomplete on all input fields
    $('input').attr('autocomplete', 'off');

    initialize_ajax_datepickers(level)
    initialize_ajax_tinymce()
})

function handle_messagelist(messagelist) {
    // messagelist: 0='message', 1='color', 2='short or long', 3='ajax or http', 4='link', 5='linkdescription'

    // let m_width = '450px';
    let m_width = 'auto';
    let m_position = 'top-right';
    let m_autohide = true;
    let m_link = ''
    let m_stacking = true
    let m_delay = 5000

    if (messagelist) {  // If there is a link to show
        if (messagelist[2] === 'short') {
            m_delay = 1000;
        }
        if (messagelist[4]&&messagelist[5]) {
            m_width = 'auto';
            m_position = 'bottom-right';
            m_autohide = false;
            if (messagelist[3]==='http') { messagelist[4] = "https://" + messagelist[4]}
            m_link = `<a href="` + messagelist[4] + ` ">` + messagelist[5] + `</a>`
        } else if (messagelist[3]) {
            m_width = 'auto';
            m_position = 'bottom-right';
            m_autohide = false;
        }

        const alert = document.createElement('div');
        alert.innerHTML =
            `
                <div class="d-flex justify-content-between">
                    <p class="mb-0">` + messagelist[0] + `</p> <p class="mb-0 ps-2 pe-2">` + m_link + `</p>
                    <button type="button" class="btn-close" data-mdb-dismiss="alert" aria-label="Close"></button>
                </div>
            `;
        alert.classList.add('alert', 'fade');

        document.body.appendChild(alert);

        const alertInstance = new mdb.Alert(alert, {
            color: messagelist[1],
            stacking: m_stacking,
            hidden: true,
            width: m_width,
            position: m_position,
            autohide: m_autohide,
            delay: m_delay,
        });

        alertInstance.show();
    }
}

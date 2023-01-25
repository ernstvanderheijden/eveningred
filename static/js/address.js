function addressVisible() {  // Is used
    if (document.getElementById("td_street").style.display === "block") {
        document.getElementById("td_street").style.display = "none";
        document.getElementById("label_street").style.display = "none";
        document.getElementById("td_city").style.display = "none";
        document.getElementById("label_city").style.display = "none";
        document.getElementById("td_latitude").style.display = "none";
        document.getElementById("label_latitude").style.display = "none";
        document.getElementById("td_longitude").style.display = "none";
        document.getElementById("label_longitude").style.display = "none";
        document.getElementById("div_address").style.display = "block";
    } else {
        document.getElementById("td_street").style.display = "block";
        document.getElementById("label_street").style.display = "block";
        document.getElementById("td_city").style.display = "block";
        document.getElementById("label_city").style.display = "block";
        document.getElementById("td_latitude").style.display = "block";
        document.getElementById("label_latitude").style.display = "block";
        document.getElementById("td_longitude").style.display = "block";
        document.getElementById("label_longitude").style.display = "block";
        document.getElementById("div_address").style.display = "none";
    }
}

function clearhousenr() {  // Is used
    if (document.getElementById("td_street").style.display === "none") {
        document.getElementById("id_number").value = "";
        document.getElementById("id_suffix").value = "";
        document.getElementById("da_1").innerText = "";
        document.getElementById("da_2").innerText = "";
        document.getElementById("da_3").innerText = "";
        document.getElementById("da_6").innerText = "";
        document.getElementById("da_7").innerText = "";
    }
}

function filladdress() {  // Is used
    if (document.getElementById("td_street").style.display === "none") {
        var x = document.getElementById("td_postalcode");
        var strpostcode = document.getElementById("id_postalcode").value;
        var strhuisnr = document.getElementById("id_number").value;
        var strhuisnrtoevoeging = document.getElementById("id_suffix").value;
        if (x.style.display === "block") {
            var dataurl = "/core/get_address/?zkpostcode=" + strpostcode + "&zkhuisnr=" + strhuisnr + "&zkhuisnrtoevoeging=" + strhuisnrtoevoeging;
            $.ajax({
                url: dataurl, type: 'get', dataType: 'json',
                success: function (data) {
                    if (data.text) {
                        var text = data.text;
                        if (text.substring(2, 11) !== "exception") {
                            var obj = JSON.parse(text);
                            document.getElementById("id_postalcode").value = obj.postcode;
                            document.getElementById("id_street").value = obj.street;
                            document.getElementById("id_number").value = obj.houseNumber;
                            document.getElementById("id_suffix").value = obj.houseNumberAddition;
                            document.getElementById("id_city").value = obj.city;
                            document.getElementById("id_latitude").value = obj.latitude;
                            document.getElementById("id_longitude").value = obj.longitude;
                            var a1 = "";
                            var a2 = "";
                            var a3 = "";
                            var a4 = "";
                            var a5 = "";
                            var a6 = "";
                            var a7 = "";
                            if (obj.street !== null) {
                                a1 = obj.street;
                            }
                            if (obj.houseNumber !== null) {
                                a2 = obj.houseNumber;
                            }
                            if (obj.houseNumberAddition !== null) {
                                a3 = obj.houseNumberAddition;
                            }
                            if (obj.postcode !== null) {
                                a4 = obj.postcode;
                            }
                            if (obj.city !== null) {
                                a5 = obj.city;
                            }
                            if (obj.latitude !== null) {
                                a6 = obj.latitude;
                            }
                            if (obj.longitude !== null) {
                                a7 = obj.longitude;
                            }
                            document.getElementById("da_1").innerText = a1 + " " + a2 + a3;
                            document.getElementById("da_2").innerText = a4 + " " + a5;
                            // document.getElementById("da_3").innerText = a5;
                            document.getElementById("da_6").innerText = "Latitude: " + a6;
                            document.getElementById("da_7").innerText = "Longitude: " + a7;
                        }
                        if (text.substring(2, 11) === "exception") {
                            document.getElementById("id_street").value = "";
                            document.getElementById("id_city").value = "";
                            document.getElementById("id_latitude").value = "";
                            document.getElementById("id_longitude").value = "";
                            document.getElementById("da_1").innerText = "Adres niet gevonden, gebruik andere invoer";
                            document.getElementById("da_2").innerText = "";
                            document.getElementById("da_3").innerText = "";
                            document.getElementById("da_6").innerText = "";
                            document.getElementById("da_7").innerText = "";
                        }
                    }
                }
            });
        }
    }
}

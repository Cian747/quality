function copySecret() {
    /* Get the text field */
    var copyText = document.getElementById("secret");

    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    document.execCommand("copy");

    alert("Successfully copied Image link!");
}

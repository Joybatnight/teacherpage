var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate() {
    var username = document.getElementById("loginUser").value;
    var password = document.getElementById("loginPassword").value;
    if (username == "123" && password == "123") {
        alert("Login successfully");
        window.location = "index.html"; // Redirecting to other page.
        return false;
    }
    else {
        attempt--;// Decrementing by one.
        alert("You have left " + attempt + " attempt;");
        // Disabling fields after 3 attempts.
        if (attempt == 0) {
            document.getElementById("loginUser").disabled = true;
            document.getElementById("loginPassword").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }
}
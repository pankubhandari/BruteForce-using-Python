<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") { 
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // Debugging: Print received data
    echo "🔍 Received Username: $username, Password: $password <br>";

    if ($username === "admin" && $password === "123455") {
        echo "Login Successful!";
    } else {
        echo "Invalid username or password";
    }
} else {
    http_response_code(405);
    echo "Method Not Allowed! Use POST.";
}
?>

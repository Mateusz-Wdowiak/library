<?php
session_start();
$host = "localhost";
$db = "users";
$user = "root";
$password = "";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $email = trim($_POST["email"]);
        $pass = trim($_POST["password"]);

        if (empty($email) || empty($pass)) {
            header("Location: login.php?error=Pola nie mogą być puste");
            exit();
        }

        $stmt = $pdo->prepare("SELECT id, username, password FROM users WHERE email = :email");
        $stmt->bindParam(":email", $email);
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($pass, $user["password"])) {
            $_SESSION["user_id"] = $user["id"];
            $_SESSION["username"] = $user["username"];

            header("Location: main.php");
            exit();
        } else {
            header("Location: login.php?error=Nieprawidłowy email lub hasło");
            exit();
        }
    }
} catch (PDOException $e) {
    die("Błąd połączenia z bazą: " . $e->getMessage());
}
?>

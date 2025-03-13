<?php
$host = "localhost";
$db = "users";
$user = "root";
$password = "";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = trim($_POST["username"]);
        $email = trim($_POST["email"]);
        $pass = trim($_POST["password"]);
        $pass_confirm = trim($_POST["password_confirm"]);

        if (empty($username) || empty($email) || empty($pass) || empty($pass_confirm)) {
            die("Pola nie mogą być puste");
        }

        if ($pass !== $pass_confirm) {
            die("Hasła się nie zgadzają");
        }

        // Sprawdzenie, czy email już istnieje
        $stmt = $pdo->prepare("SELECT id FROM users WHERE email = :email");
        $stmt->bindParam(":email", $email);
        $stmt->execute();
        if ($stmt->fetch()) {
         header("Location: register.php?error=Adres email jest już zajęty");
         exit();
        }

        // Hashowanie hasła i zapis do bazy
        $hashed_password = password_hash($pass, PASSWORD_DEFAULT);

        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->bindParam(":username", $username);
        $stmt->bindParam(":email", $email);
        $stmt->bindParam(":password", $hashed_password);

        if ($stmt->execute()) {
            echo "Konto zostało zarejestrowane";
            header("Location: main.php");
            exit();
        } else {
            echo "Coś poszło nie tak. Spróbuj ponownie";
        }
    }
} catch (PDOException $e) {
    header("Location: register.php?error=Błąd serwera, spróbuj później.");
    exit();
}
?>

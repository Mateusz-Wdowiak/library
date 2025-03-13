<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biblioteka Uczelni WSB</title>

<style>
    @import URL("styl.css");
</style>
</head>
<body>
    

<div class="banner">
    <h1>WSB MERITO BIBLIOTEKA</h1>
</div>
  <div id="form">
  <form method="POST" action="login_pdo.php" onsubmit="return validate()">
<br><br>
      <h2 id="log_h2">Adres email</h2>
      <input type="email" name="email" id="log_email" placeholder="PODAJ SWÓJ EMAIL">

      <h2 id="log_h2">Hasło</h2>
      <input type="password" name="password" id="log_password" placeholder="PODAJ SWOJE HASŁO">

      <br><br>
      <input type="submit" id="log_button" value="Login">

      <h4>Nie masz konta?</h4><a id ="register_link" href="register.php">Zarejestruj się</a>
      <p id="error-message2" style="color: red; font-weight: bold; display: <?php echo isset($_GET['error']) ? 'block' : 'none'; ?>;">
    <?php if (isset($_GET['error'])) echo htmlspecialchars($_GET['error']); ?>
</p>
    </form>
    <script>
      function validate(){
      var pass = document.getElementById("password").value;
      var conf_pass = document.getElementById("password_confirm").value
      var error = document.getElementById("error-message");
        if(pass == conf_pass){
          error.style.display = "none";
          return true;
        }else{
          error.style.display = "block";
          return false;
        }
      }
    </script>
</div>
</body>
</html>

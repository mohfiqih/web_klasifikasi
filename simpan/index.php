<?php

$output = shell_exec("python /xampp/htdocs/web_klasifikasi/coba.py");
echo $output;

?>
<!-- 
<html>

<body>

     <head>
          <title>
               run
          </title>
     </head>

     <form method="post">
          <input type="text" placeholder="Masukan text">
          <input type="submit" value="Klik" name="post">
     </form>
</body>

</html>

<?php
	if(isset($_POST['post']))
	{
		$py = shell_exec("python /xampp/htdocs/web_klasifikasi/coba.py");
		echo "$py";
	}
?> -->
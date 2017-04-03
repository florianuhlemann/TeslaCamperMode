<?php
	if (isset($_POST['password'])) {
		if ($_POST['password'] == "YOUR_PASSWORD") { //Please change the password to your desired password.
			if ($_POST['command'] == "start") {
				$myfile = fopen("is_currently_heating", "w") or die("Unable to open file!");
				fclose($myfile);
			} elseif ($_POST['command'] == "stop") {
				unlink("is_currently_heating");
			}
		}
	}	
?>